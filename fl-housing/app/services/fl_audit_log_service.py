"""审计日志服务"""
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.fl_audit_log import FlAuditLog


class FlAuditLogService:
    # 需要记录日志的模块映射
    MODULE_MAP = {
        "/auth/": "用户认证",
        "/user/": "用户管理",
        "/admin/": "管理后台",
        "/content/": "内容管理",
        "/developer/": "开发商",
        "/house/": "房源管理",
        "/deposit/": "定金托管",
        "/talent/": "人才认证",
    }
    
    # 操作事项映射
    ACTION_MAP = {
        ("POST", "/auth/register"): "用户注册",
        ("POST", "/auth/login"): "用户登录",
        ("POST", "/auth/send_sms"): "发送验证码",
        ("GET", "/user/profile"): "获取用户信息",
        ("PUT", "/user/profile"): "更新用户信息",
        ("POST", "/user/verify/idcard"): "身份证认证",
        ("POST", "/user/verify/credit_score"): "信用分认证",
        ("POST", "/user/verify/education"): "学历认证",
        ("GET", "/admin/user/list"): "查看用户列表",
        ("GET", "/admin/user/"): "查看用户详情",
        ("POST", "/admin/user/"): "分配用户角色",
        ("DELETE", "/admin/user/"): "撤销用户角色",
    }
    
    def get_module(self, path: str) -> str:
        """根据路径获取模块名"""
        for prefix, module in self.MODULE_MAP.items():
            if prefix in path:
                return module
        return "其他"
    
    def get_action(self, method: str, path: str) -> str:
        """根据方法和路径获取操作事项"""
        # 精确匹配
        key = (method, path)
        if key in self.ACTION_MAP:
            return self.ACTION_MAP[key]
        # 前缀匹配
        for (m, p), action in self.ACTION_MAP.items():
            if method == m and path.startswith(p):
                return action
        return f"{method} {path}"
    
    def create_log(self, db: Session, log_data: dict) -> FlAuditLog:
        """创建操作日志"""
        log = FlAuditLog(**log_data)
        db.add(log)
        db.commit()
        return log
    
    def get_log_list(self, db: Session, page: int = 1, page_size: int = 20,
                     module: str = None, username: str = None, 
                     start_date: str = None, end_date: str = None) -> dict:
        """查询操作日志列表"""
        query = db.query(FlAuditLog)
        
        if module:
            query = query.filter(FlAuditLog.module == module)
        if username:
            query = query.filter(
                or_(
                    FlAuditLog.username.like(f"%{username}%"),
                    FlAuditLog.user_id == username if username.isdigit() else False
                )
            )
        if start_date:
            query = query.filter(FlAuditLog.created_at >= start_date)
        if end_date:
            query = query.filter(FlAuditLog.created_at <= end_date + " 23:59:59")
        
        total = query.count()
        logs = query.order_by(FlAuditLog.id.desc()).offset((page - 1) * page_size).limit(page_size).all()
        
        return {
            "list": [self._log_dict(log) for log in logs],
            "total": total,
            "page": page,
            "page_size": page_size
        }
    
    def _log_dict(self, log: FlAuditLog) -> dict:
        return {
            "id": log.id,
            "user_id": log.user_id,
            "username": log.username,
            "module": log.module,
            "action": log.action,
            "method": log.method,
            "path": log.path,
            "ip": log.ip,
            "response_code": log.response_code,
            "duration_ms": log.duration_ms,
            "created_at": log.created_at.strftime("%Y-%m-%d %H:%M:%S") if log.created_at else None
        }


fl_audit_log_service = FlAuditLogService()
