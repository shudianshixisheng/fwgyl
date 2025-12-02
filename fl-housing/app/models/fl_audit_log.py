"""审计日志模型"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.core.database import Base


class FlAuditLog(Base):
    """操作日志表"""
    __tablename__ = "audit_log"
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, comment="操作用户ID")
    username = Column(String(50), comment="用户名/手机号")
    module = Column(String(50), comment="操作模块")
    action = Column(String(100), comment="操作事项")
    method = Column(String(10), comment="请求方法")
    path = Column(String(200), comment="请求路径")
    ip = Column(String(50), comment="请求IP")
    user_agent = Column(String(500), comment="User-Agent")
    request_body = Column(Text, comment="请求体")
    response_code = Column(Integer, comment="响应状态码")
    duration_ms = Column(Integer, comment="耗时(毫秒)")
    created_at = Column(DateTime, default=datetime.utcnow, comment="创建时间")
