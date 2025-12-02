"""Day1: 用户Schema"""
from typing import Optional
from pydantic import BaseModel, Field


class FlSendSmsRequest(BaseModel):
    phone: str = Field(..., pattern=r"^1[3-9]\d{9}$")
    scene: str = Field(..., pattern=r"^(register|login|reset_password)$")


class FlRegisterRequest(BaseModel):
    phone: str = Field(..., pattern=r"^1[3-9]\d{9}$", description="手机号")
    sms_code: str = Field(..., min_length=4, max_length=6, description="短信验证码")
    password: str = Field(..., min_length=6, max_length=20, description="密码")
    username: Optional[str] = Field(None, min_length=4, max_length=20, description="用户名（可选，用于登录）")
    nickname: Optional[str] = Field(None, max_length=20, description="昵称（可选，默认用户+手机后4位）")


class FlLoginRequest(BaseModel):
    account: str
    password: Optional[str] = None
    sms_code: Optional[str] = None
    login_type: str = "password"


class FlUserProfileUpdate(BaseModel):
    nickname: Optional[str] = None
    username: Optional[str] = None


class FlIdcardVerifyRequest(BaseModel):
    """身份证二要素认证：姓名+身份证号"""
    real_name: str = Field(..., description="真实姓名")
    id_card_no: str = Field(..., min_length=18, max_length=18, description="身份证号")


class FlCreditScoreVerifyRequest(BaseModel):
    """信用分认证：选择来源，授权后系统自动获取分数"""
    credit_source: str = Field(..., pattern=r"^(zhima|wechat_pay)$", description="信用分来源：zhima(芝麻信用) / wechat_pay(微信支付分)")


class FlEducationVerifyRequest(BaseModel):
    """学历认证：提交学信网在线验证码"""
    verification_code: str = Field(..., min_length=10, max_length=20, description="学信网在线验证码（12位）")


class FlUserListQuery(BaseModel):
    page: int = 1
    page_size: int = 20
    phone: Optional[str] = None
    username: Optional[str] = None
    user_level: Optional[str] = None
    status: Optional[str] = None
