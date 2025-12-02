"""Day1: 认证API"""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.response import fl_success
from app.schemas.fl_user_schema import FlSendSmsRequest, FlRegisterRequest, FlLoginRequest
from app.services.fl_user_service import fl_user_service

router = APIRouter(prefix="/auth", tags=["认证"])


@router.post("/send_sms")
def send_sms(req: FlSendSmsRequest, db: Session = Depends(get_db)):
    """
    发送短信验证码
    【模拟】验证码打印到控制台，万能验证码666666
    【正式】需开通阿里云短信服务API
    """
    return fl_success(fl_user_service.send_sms(db, req), "验证码发送成功")


@router.post("/register")
def register(req: FlRegisterRequest, db: Session = Depends(get_db)):
    """用户注册"""
    return fl_success(fl_user_service.register(db, req), "注册成功")


@router.post("/login")
def login(req: FlLoginRequest, request: Request, db: Session = Depends(get_db)):
    """
    用户登录
    login_type: password(密码) / sms(验证码)
    """
    ip = request.client.host if request.client else "unknown"
    return fl_success(fl_user_service.login(db, req, ip), "登录成功")
