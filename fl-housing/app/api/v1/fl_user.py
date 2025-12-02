"""Day1: 用户API"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.response import fl_success
from app.core.dependencies import get_current_user, require_admin, FlCurrentUser
from app.schemas.fl_user_schema import *
from app.services.fl_user_service import fl_user_service

router = APIRouter(prefix="/user", tags=["用户"])


@router.get("/profile")
def get_profile(user: FlCurrentUser = Depends(get_current_user), db: Session = Depends(get_db)):
    """获取当前用户信息"""
    return fl_success(fl_user_service.get_profile(db, user.user_id))


@router.put("/profile/update")
def update_profile(req: FlUserProfileUpdate, user: FlCurrentUser = Depends(get_current_user), db: Session = Depends(get_db)):
    """更新用户信息"""
    return fl_success(fl_user_service.update_profile(db, user.user_id, req), "更新成功")


@router.post("/verify/idcard")
def verify_idcard(req: FlIdcardVerifyRequest, user: FlCurrentUser = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    身份证实名认证
    【模拟】直接通过
    【正式】需开通阿里云实名认证API或腾讯云人脸核身API
    """
    return fl_success(fl_user_service.verify_idcard(db, user.user_id, req), "认证成功")


@router.post("/verify/credit_score")
def verify_credit_score(req: FlCreditScoreVerifyRequest, user: FlCurrentUser = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    信用分认证
    【模拟】使用用户提交的分数
    【正式】需开通芝麻信用API或微信支付分API
    """
    return fl_success(fl_user_service.verify_credit_score(db, user.user_id, req), "认证成功")


@router.post("/verify/education")
def verify_education(req: FlEducationVerifyRequest, user: FlCurrentUser = Depends(get_current_user), db: Session = Depends(get_db)):
    """学历认证提交"""
    return fl_success(fl_user_service.verify_education(db, user.user_id, req), "提交成功，等待审核")


admin_router = APIRouter(prefix="/admin", tags=["管理后台"])


@admin_router.get("/user/list")
def get_user_list(
    page: int = Query(1),
    page_size: int = Query(20),
    phone: str = Query(None),
    username: str = Query(None),
    user_level: str = Query(None),
    status: str = Query(None),
    user: FlCurrentUser = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """[管理员]用户列表"""
    return fl_success(fl_user_service.get_user_list(db, FlUserListQuery(
        page=page, page_size=page_size, phone=phone, username=username, user_level=user_level, status=status
    )))


@admin_router.get("/user/{user_id}")
def get_user_detail(user_id: int, user: FlCurrentUser = Depends(require_admin), db: Session = Depends(get_db)):
    """[管理员]查看用户详情"""
    return fl_success(fl_user_service.get_user_detail(db, user_id))


@admin_router.post("/user/{user_id}/assign_role")
def assign_role(user_id: int, role_code: str = Query(...), user: FlCurrentUser = Depends(require_admin), db: Session = Depends(get_db)):
    """[管理员]给用户分配角色"""
    return fl_success(fl_user_service.assign_role(db, user_id, role_code), "角色分配成功")


@admin_router.delete("/user/{user_id}/remove_role")
def remove_role(user_id: int, role_code: str = Query(...), user: FlCurrentUser = Depends(require_admin), db: Session = Depends(get_db)):
    """[管理员]撤销用户角色"""
    return fl_success(fl_user_service.remove_role(db, user_id, role_code), "角色撤销成功")
