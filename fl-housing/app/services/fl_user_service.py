"""Day1: 用户服务"""
from datetime import datetime, timedelta
from sqlalchemy.orm import Session, joinedload
from app.models.fl_user import FlUser, FlUserVerification, FlRole, FlUserRole
from app.schemas.fl_user_schema import *
from app.core.security import fl_security
from app.core.exceptions import FlBadRequest, FlNotFound
from app.utils.sms import fl_sms
from app.utils.validators import fl_validator


class FlUserService:
    def send_sms(self, db: Session, req: FlSendSmsRequest) -> dict:
        code = fl_sms.generate_code()
        fl_sms.send(req.phone, code)
        return {"expire_seconds": 300}
    
    def register(self, db: Session, req: FlRegisterRequest) -> dict:
        if not fl_sms.verify(req.phone, req.sms_code):
            raise FlBadRequest("验证码错误或已过期")
        if db.query(FlUser).filter(FlUser.phone == req.phone).first():
            raise FlBadRequest("手机号已注册")
        if req.username and db.query(FlUser).filter(FlUser.username == req.username).first():
            raise FlBadRequest("用户名已存在")
        user = FlUser(
            phone=req.phone,
            username=req.username,
            password_hash=fl_security.hash_password(req.password),
            nickname=req.nickname or f"用户{req.phone[-4:]}",
            user_level="normal"
        )
        db.add(user)
        db.flush()
        role = db.query(FlRole).filter(FlRole.role_code == "ROLE_NORMAL_USER").first()
        if role:
            db.add(FlUserRole(user_id=user.id, role_id=role.id))
        db.commit()
        roles = ["ROLE_NORMAL_USER"]
        token = fl_security.create_token(user.id, roles)
        return {
            "user_id": user.id,
            "phone": fl_validator.mask_phone(user.phone),
            "nickname": user.nickname,
            "roles": roles,
            "token": token
        }
    
    def login(self, db: Session, req: FlLoginRequest, ip: str) -> dict:
        user = db.query(FlUser).options(
            joinedload(FlUser.roles).joinedload(FlUserRole.role)
        ).filter(
            (FlUser.phone == req.account) | (FlUser.username == req.account)
        ).first()
        if not user:
            raise FlBadRequest("用户不存在")
        if user.status != "active":
            raise FlBadRequest("账号已被禁用")
        if req.login_type == "password":
            if not fl_security.verify_password(req.password, user.password_hash):
                raise FlBadRequest("密码错误")
        elif req.login_type == "sms":
            if not fl_sms.verify(req.account, req.sms_code):
                raise FlBadRequest("验证码错误或已过期")
        user.last_login_at = datetime.utcnow()
        user.last_login_ip = ip
        db.commit()
        roles = [ur.role.role_code for ur in user.roles]
        token = fl_security.create_token(user.id, roles)
        return {
            "user_id": user.id,
            "phone": fl_validator.mask_phone(user.phone),
            "nickname": user.nickname,
            "user_level": user.user_level,
            "roles": roles,
            "token": token
        }
    
    def get_profile(self, db: Session, user_id: int) -> dict:
        user = db.query(FlUser).options(
            joinedload(FlUser.roles).joinedload(FlUserRole.role)
        ).filter(FlUser.id == user_id).first()
        if not user:
            raise FlNotFound("用户不存在")
        roles = [ur.role.role_code for ur in user.roles]
        return {
            "user_id": user.id,
            "phone": fl_validator.mask_phone(user.phone),
            "username": user.username,
            "nickname": user.nickname,
            "user_level": user.user_level,
            "credit_score": user.credit_score,
            "roles": roles,
            "status": user.status
        }
    
    def update_profile(self, db: Session, user_id: int, req: FlUserProfileUpdate) -> dict:
        user = db.query(FlUser).filter(FlUser.id == user_id).first()
        if not user:
            raise FlNotFound("用户不存在")
        # 验证手机号是否与当前用户匹配
        if req.phone != user.phone:
            # 检查新手机号是否已被占用
            if db.query(FlUser).filter(FlUser.phone == req.phone, FlUser.id != user_id).first():
                raise FlBadRequest("该手机号已被其他用户使用")
            user.phone = req.phone
        if req.nickname:
            user.nickname = req.nickname
        if req.username:
            if db.query(FlUser).filter(FlUser.username == req.username, FlUser.id != user_id).first():
                raise FlBadRequest("用户名已存在")
            user.username = req.username
        db.commit()
        return {"user_id": user_id, "phone": user.phone, "nickname": user.nickname, "username": user.username}
    
    def verify_idcard(self, db: Session, user_id: int, req: FlIdcardVerifyRequest) -> dict:
        """
        身份证实名认证
        【模拟】直接通过，正式环境需调用实名认证API
        """
        from app.utils.idcard import fl_idcard
        result = fl_idcard.verify_two_elements(req.real_name, req.id_card_no)
        if not result["success"]:
            raise FlBadRequest(result["message"])
        v = FlUserVerification(
            user_id=user_id,
            verify_type="idcard",
            real_name=req.real_name,
            id_card_no=req.id_card_no,
            verify_status="approved",  # 模拟：直接通过
            verified_at=datetime.utcnow()
        )
        db.add(v)
        # 身份证认证通过后，升级为实名用户（可选其一方式完成实名认证）
        user = db.query(FlUser).filter(FlUser.id == user_id).first()
        user.user_level = "verified"
        role = db.query(FlRole).filter(FlRole.role_code == "ROLE_VERIFIED_USER").first()
        if role:
            exists = db.query(FlUserRole).filter(FlUserRole.user_id == user_id, FlUserRole.role_id == role.id).first()
            if not exists:
                db.add(FlUserRole(user_id=user_id, role_id=role.id))
        db.commit()
        return {"verification_id": v.id, "verify_type": "idcard", "verify_status": "approved", "user_level": "verified"}
    
    def verify_credit_score(self, db: Session, user_id: int, req: FlCreditScoreVerifyRequest) -> dict:
        """
        信用分认证
        【模拟】返回模拟分数，正式环境需用户授权后调用芝麻/微信支付分API获取
        """
        from app.utils.credit import fl_credit
        # 模拟：根据来源返回模拟分数
        if req.credit_source == "zhima":
            result = fl_credit.query_zhima_score(user_id)
        else:
            result = fl_credit.query_wechat_score(user_id)
        mock_score = result["score"]
        
        v = FlUserVerification(
            user_id=user_id,
            verify_type="credit_score",
            credit_score=mock_score,
            credit_source=req.credit_source,
            verify_status="approved",
            verified_at=datetime.utcnow()
        )
        db.add(v)
        user = db.query(FlUser).filter(FlUser.id == user_id).first()
        user.user_level = "verified"
        user.credit_score = mock_score
        role = db.query(FlRole).filter(FlRole.role_code == "ROLE_VERIFIED_USER").first()
        if role:
            exists = db.query(FlUserRole).filter(FlUserRole.user_id == user_id, FlUserRole.role_id == role.id).first()
            if not exists:
                db.add(FlUserRole(user_id=user_id, role_id=role.id))
        db.commit()
        return {
            "verification_id": v.id, 
            "verify_type": "credit_score", 
            "verify_status": "approved", 
            "credit_score": mock_score,
            "credit_source": req.credit_source,
            "user_level": "verified"
        }
    
    def verify_education(self, db: Session, user_id: int, req: FlEducationVerifyRequest) -> dict:
        """
        学历认证
        【模拟】直接通过并返回模拟学历，正式环境需调用学信网API验证
        """
        from app.utils.education import fl_education
        # 模拟：验证码格式校验，返回模拟学历信息
        result = fl_education.verify_by_code(req.verification_code)
        if not result["success"]:
            raise FlBadRequest(result["message"])
        
        v = FlUserVerification(
            user_id=user_id,
            verify_type="education",
            education_level=result["data"]["education_level"],
            verify_status="approved",  # 模拟：直接通过
            verified_at=datetime.utcnow()
        )
        db.add(v)
        # 学历认证通过后，升级为实名用户（可选其一方式完成实名认证）
        user = db.query(FlUser).filter(FlUser.id == user_id).first()
        user.user_level = "verified"
        role = db.query(FlRole).filter(FlRole.role_code == "ROLE_VERIFIED_USER").first()
        if role:
            exists = db.query(FlUserRole).filter(FlUserRole.user_id == user_id, FlUserRole.role_id == role.id).first()
            if not exists:
                db.add(FlUserRole(user_id=user_id, role_id=role.id))
        db.commit()
        return {
            "verification_id": v.id, 
            "verify_type": "education", 
            "verify_status": "approved",
            "education_level": result["data"]["education_level"],
            "education_name": result["data"]["education_name"],
            "user_level": "verified"
        }
    
    def get_user_list(self, db: Session, q: FlUserListQuery) -> dict:
        query = db.query(FlUser)
        if q.phone:
            query = query.filter(FlUser.phone.like(f"%{q.phone}%"))
        if q.username:
            query = query.filter(FlUser.username.like(f"%{q.username}%"))
        if q.user_level:
            query = query.filter(FlUser.user_level == q.user_level)
        if q.status:
            query = query.filter(FlUser.status == q.status)
        total = query.count()
        users = query.order_by(FlUser.id.desc()).offset((q.page - 1) * q.page_size).limit(q.page_size).all()
        return {
            "list": [self._user_dict(u) for u in users],
            "total": total,
            "page": q.page,
            "page_size": q.page_size
        }
    
    def _user_dict(self, u: FlUser) -> dict:
        return {
            "user_id": u.id,
            "phone": u.phone,
            "username": u.username,
            "nickname": u.nickname,
            "user_level": u.user_level,
            "status": u.status,
            "created_at": u.created_at.isoformat() if u.created_at else None
        }
    
    def get_user_detail(self, db: Session, user_id: int) -> dict:
        """[管理员]获取用户详情，包含角色列表"""
        user = db.query(FlUser).options(
            joinedload(FlUser.roles).joinedload(FlUserRole.role)
        ).filter(FlUser.id == user_id).first()
        if not user:
            raise FlNotFound("用户不存在")
        roles = [{"role_id": ur.role.id, "role_code": ur.role.role_code, "role_name": ur.role.role_name} for ur in user.roles]
        return {
            "user_id": user.id,
            "phone": user.phone,
            "username": user.username,
            "nickname": user.nickname,
            "user_level": user.user_level,
            "credit_score": user.credit_score,
            "status": user.status,
            "roles": roles,
            "created_at": user.created_at.isoformat() if user.created_at else None,
            "last_login_at": user.last_login_at.isoformat() if user.last_login_at else None
        }
    
    def assign_role(self, db: Session, user_id: int, role_code: str) -> dict:
        """[管理员]给用户分配角色"""
        user = db.query(FlUser).filter(FlUser.id == user_id).first()
        if not user:
            raise FlNotFound("用户不存在")
        role = db.query(FlRole).filter(FlRole.role_code == role_code).first()
        if not role:
            raise FlBadRequest(f"角色不存在: {role_code}")
        exists = db.query(FlUserRole).filter(FlUserRole.user_id == user_id, FlUserRole.role_id == role.id).first()
        if exists:
            raise FlBadRequest("用户已拥有该角色")
        db.add(FlUserRole(user_id=user_id, role_id=role.id))
        db.commit()
        return {"user_id": user_id, "role_code": role_code, "role_name": role.role_name}
    
    def remove_role(self, db: Session, user_id: int, role_code: str) -> dict:
        """[管理员]撤销用户角色"""
        user = db.query(FlUser).filter(FlUser.id == user_id).first()
        if not user:
            raise FlNotFound("用户不存在")
        role = db.query(FlRole).filter(FlRole.role_code == role_code).first()
        if not role:
            raise FlBadRequest(f"角色不存在: {role_code}")
        user_role = db.query(FlUserRole).filter(FlUserRole.user_id == user_id, FlUserRole.role_id == role.id).first()
        if not user_role:
            raise FlBadRequest("用户没有该角色")
        db.delete(user_role)
        db.commit()
        return {"user_id": user_id, "role_code": role_code, "removed": True}


fl_user_service = FlUserService()
