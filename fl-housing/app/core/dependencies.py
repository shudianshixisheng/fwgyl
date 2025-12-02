from typing import Optional
from fastapi import Depends, Header
from app.core.security import fl_security
from app.core.exceptions import FlUnauthorized, FlForbidden


class FlCurrentUser:
    def __init__(self, user_id: int, roles: list):
        self.user_id = user_id
        self.roles = roles
    
    def has_role(self, role: str) -> bool:
        return role in self.roles
    
    def is_admin(self) -> bool:
        return "ROLE_ADMIN" in self.roles
    
    def is_operator(self) -> bool:
        return "ROLE_OPERATOR" in self.roles or self.is_admin()
    
    def is_developer(self) -> bool:
        return "ROLE_DEVELOPER" in self.roles
    
    def is_verified(self) -> bool:
        return "ROLE_VERIFIED_USER" in self.roles or self.is_developer() or self.is_operator()


def get_current_user(authorization: Optional[str] = Header(None)) -> FlCurrentUser:
    if not authorization:
        raise FlUnauthorized()
    # 去掉 Bearer 前缀
    token = authorization.replace("Bearer ", "").replace("bearer ", "")
    payload = fl_security.decode_token(token)
    if not payload:
        raise FlUnauthorized()
    return FlCurrentUser(user_id=int(payload["sub"]), roles=payload.get("roles", []))


def get_current_user_optional(authorization: Optional[str] = Header(None)) -> Optional[FlCurrentUser]:
    if not authorization:
        return None
    token = authorization.replace("Bearer ", "").replace("bearer ", "")
    payload = fl_security.decode_token(token)
    return FlCurrentUser(user_id=int(payload["sub"]), roles=payload.get("roles", [])) if payload else None


def require_roles(*required_roles: str):
    def checker(user: FlCurrentUser = Depends(get_current_user)):
        if not any(user.has_role(r) for r in required_roles) and not user.is_admin():
            raise FlForbidden()
        return user
    return checker


require_admin = require_roles("ROLE_ADMIN")
require_operator = require_roles("ROLE_OPERATOR", "ROLE_ADMIN")
require_developer = require_roles("ROLE_DEVELOPER")
require_verified = require_roles("ROLE_VERIFIED_USER", "ROLE_DEVELOPER", "ROLE_OPERATOR", "ROLE_ADMIN")
