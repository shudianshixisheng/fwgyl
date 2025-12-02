"""
数据校验工具
"""
import re
from app.core.exceptions import FlBadRequest


class FlValidator:
    PHONE_PATTERN = re.compile(r"^1[3-9]\d{9}$")
    IDCARD_PATTERN = re.compile(r"^\d{17}[\dXx]$")
    XSS_PATTERN = re.compile(r'<script[^>]*>.*?</script>', re.IGNORECASE | re.DOTALL)
    DANGEROUS_EXTENSIONS = {"exe", "bat", "sh", "cmd", "ps1", "vbs", "js", "jar", "php"}
    
    def check_phone(self, phone: str) -> bool:
        if not self.PHONE_PATTERN.match(phone):
            raise FlBadRequest("手机号格式错误")
        return True
    
    def check_idcard(self, idcard: str) -> bool:
        if not self.IDCARD_PATTERN.match(idcard):
            raise FlBadRequest("身份证号格式错误")
        return True
    
    def check_xss(self, text: str) -> bool:
        if self.XSS_PATTERN.search(text):
            raise FlBadRequest("内容包含不安全脚本")
        return True
    
    def check_file_ext(self, filename: str) -> bool:
        ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
        if ext in self.DANGEROUS_EXTENSIONS:
            raise FlBadRequest("不允许上传此类型文件")
        return True
    
    def mask_phone(self, phone: str) -> str:
        if not phone or len(phone) != 11:
            return phone
        return f"{phone[:3]}****{phone[-4:]}"
    
    def mask_idcard(self, idcard: str) -> str:
        if not idcard or len(idcard) != 18:
            return idcard
        return f"{idcard[:6]}********{idcard[-4:]}"
    
    def mask_name(self, name: str) -> str:
        if not name:
            return name
        if len(name) <= 2:
            return name[0] + "*"
        return name[0] + "*" * (len(name) - 2) + name[-1]


fl_validator = FlValidator()
