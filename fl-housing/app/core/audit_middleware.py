"""审计日志中间件"""
import time
import json
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.database import SessionLocal
from app.services.fl_audit_log_service import fl_audit_log_service


class AuditLogMiddleware(BaseHTTPMiddleware):
    """自动记录操作日志的中间件"""
    
    # 需要记录日志的路径前缀
    LOG_PATHS = ["/api/v1/auth/", "/api/v1/user/", "/api/v1/admin/"]
    
    # 排除的路径（不记录日志）
    EXCLUDE_PATHS = ["/api/v1/auth/send_sms", "/static/", "/uploads/", "/docs", "/openapi.json"]
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # 检查是否需要记录日志
        path = request.url.path
        should_log = any(path.startswith(p) for p in self.LOG_PATHS)
        should_log = should_log and not any(path.startswith(p) for p in self.EXCLUDE_PATHS)
        
        # 获取请求体
        request_body = None
        if should_log and request.method in ["POST", "PUT", "PATCH"]:
            try:
                body = await request.body()
                request_body = body.decode("utf-8")[:1000]  # 限制长度
                # 隐藏敏感信息
                if "password" in request_body.lower():
                    try:
                        body_dict = json.loads(request_body)
                        if "password" in body_dict:
                            body_dict["password"] = "***"
                        request_body = json.dumps(body_dict, ensure_ascii=False)
                    except:
                        pass
            except:
                pass
        
        # 执行请求
        response = await call_next(request)
        
        # 记录日志
        if should_log:
            duration_ms = int((time.time() - start_time) * 1000)
            
            # 获取用户信息
            user_id = None
            username = None
            auth_header = request.headers.get("Authorization", "")
            if auth_header.startswith("Bearer "):
                try:
                    from app.core.security import fl_security
                    token = auth_header[7:]
                    payload = fl_security.decode_token(token)
                    if payload:
                        user_id = payload.get("sub")
                except:
                    pass
            
            # 获取IP
            ip = request.headers.get("X-Forwarded-For", request.client.host if request.client else "unknown")
            if "," in ip:
                ip = ip.split(",")[0].strip()
            
            # 获取模块和操作
            api_path = path.replace("/api/v1", "")
            module = fl_audit_log_service.get_module(api_path)
            action = fl_audit_log_service.get_action(request.method, api_path)
            
            # 异步记录日志（不阻塞响应）
            try:
                db = SessionLocal()
                fl_audit_log_service.create_log(db, {
                    "user_id": user_id,
                    "username": username,
                    "module": module,
                    "action": action,
                    "method": request.method,
                    "path": api_path,
                    "ip": ip,
                    "user_agent": request.headers.get("User-Agent", "")[:500],
                    "request_body": request_body,
                    "response_code": response.status_code,
                    "duration_ms": duration_ms
                })
                db.close()
            except Exception as e:
                print(f"记录审计日志失败: {e}")
        
        return response
