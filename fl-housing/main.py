"""
陵水住房供应链平台 - 后端服务

【模拟接口说明】
以下第三方接口当前为模拟实现，正式上线需开通对应API权限：

1. 短信服务 (app/utils/sms.py)
   - 模拟：验证码打印到控制台，万能验证码666666
   - 正式：需开通阿里云短信服务API
     * 申请短信签名
     * 申请验证码模板
     * 获取AccessKey

2. 支付服务 (app/utils/payment.py)
   - 模拟：直接返回支付成功
   - 正式：需开通以下支付渠道
     * 微信支付商户号及API密钥
     * 支付宝开放平台应用
     * 完成ICP备案

3. 实名认证 (app/utils/idcard.py)
   - 模拟：直接返回验证通过
   - 正式：需开通以下API
     * 阿里云实名认证API
     * 或腾讯云人脸核身API

4. 信用分查询 (app/utils/credit.py)
   - 模拟：返回随机信用分
   - 正式：需开通以下API
     * 芝麻信用API（需企业资质）
     * 或微信支付分API
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="陵水住房供应链平台API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_DIR), name="uploads")

# 挂载静态调试页面
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")

# 初始化数据库（导入所有模型后自动建表）
from app.core.database import Base, engine, init_db
# 导入所有模型以创建表
from app.models.fl_user import FlUser, FlRole, FlUserRole, FlUserVerification
from app.models.fl_content import FlContent
from app.models.fl_developer import FlCompany, FlProject
from app.models.fl_house import FlHouse
from app.models.fl_deposit import FlDepositContractTemplate, FlDepositOrder
from app.models.fl_talent import FlTalentApplication
from app.models.fl_audit_log import FlAuditLog
Base.metadata.create_all(bind=engine)
init_db()

# 审计日志中间件
from app.core.audit_middleware import AuditLogMiddleware
app.add_middleware(AuditLogMiddleware)

# Day1: 认证和用户
from app.api.v1 import fl_auth, fl_user, fl_audit_log
app.include_router(fl_auth.router, prefix=settings.API_V1_PREFIX)
app.include_router(fl_user.router, prefix=settings.API_V1_PREFIX)
app.include_router(fl_user.admin_router, prefix=settings.API_V1_PREFIX)
app.include_router(fl_audit_log.router, prefix=settings.API_V1_PREFIX)

# Day2: 内容管理
from app.api.v1 import fl_content, fl_file, fl_banner
app.include_router(fl_content.router, prefix=settings.API_V1_PREFIX)
app.include_router(fl_file.router, prefix=settings.API_V1_PREFIX)
app.include_router(fl_banner.router, prefix=settings.API_V1_PREFIX)

# Day3: 开发商和审核
from app.api.v1 import fl_developer, fl_audit
app.include_router(fl_developer.router, prefix=settings.API_V1_PREFIX)
app.include_router(fl_audit.router, prefix=settings.API_V1_PREFIX)

# Day4: 房源和扫码
from app.api.v1 import fl_house, fl_scan
app.include_router(fl_house.router, prefix=settings.API_V1_PREFIX)
app.include_router(fl_scan.router, prefix=settings.API_V1_PREFIX)

# Day5: 定金托管
from app.api.v1 import fl_deposit
app.include_router(fl_deposit.router, prefix=settings.API_V1_PREFIX)

# Day6: 人才/点评/投诉
from app.api.v1 import fl_talent, fl_review, fl_complaint
app.include_router(fl_talent.router, prefix=settings.API_V1_PREFIX)
app.include_router(fl_review.router, prefix=settings.API_V1_PREFIX)
app.include_router(fl_complaint.router, prefix=settings.API_V1_PREFIX)


@app.get("/")
def root():
    return {"name": settings.APP_NAME, "status": "running"}


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
