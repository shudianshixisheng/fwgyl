import hashlib
import json
import base64
import time
import sys
sys.path.append(".")
from config import settings


class FlSecurity:
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256((password + settings.SECRET_KEY).encode()).hexdigest()
    
    @staticmethod
    def verify_password(plain: str, hashed: str) -> bool:
        return FlSecurity.hash_password(plain) == hashed
    
    @staticmethod
    def create_token(user_id: int, roles: list) -> str:
        payload = {"sub": user_id, "roles": roles, "exp": int(time.time()) + settings.TOKEN_EXPIRE_DAYS * 86400}
        data = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()
        sign = hashlib.sha256((data + settings.SECRET_KEY).encode()).hexdigest()[:16]
        return f"{data}.{sign}"
    
    @staticmethod
    def decode_token(token: str) -> dict | None:
        try:
            data, sign = token.rsplit(".", 1)
            if hashlib.sha256((data + settings.SECRET_KEY).encode()).hexdigest()[:16] != sign:
                return None
            payload = json.loads(base64.urlsafe_b64decode(data))
            if payload["exp"] < time.time():
                return None
            return payload
        except:
            return None


fl_security = FlSecurity()
