"""Day1: 用户模型"""
from datetime import datetime
from sqlalchemy import Column, BigInteger, String, Enum, DateTime, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class FlUser(Base):
    __tablename__ = "user"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    phone = Column(String(20), unique=True, nullable=False)
    username = Column(String(50), unique=True)
    password_hash = Column(String(255), nullable=False)
    nickname = Column(String(50))
    avatar_url = Column(String(500))
    user_level = Column(Enum("temp", "normal", "verified"), default="normal")
    credit_score = Column(Integer)
    status = Column(Enum("active", "disabled", "deleted"), default="active")
    last_login_at = Column(DateTime)
    last_login_ip = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    roles = relationship("FlUserRole", back_populates="user")
    verifications = relationship("FlUserVerification", back_populates="user")


class FlUserVerification(Base):
    __tablename__ = "user_verification"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False)
    verify_type = Column(Enum("idcard", "credit_score", "education"), nullable=False)
    real_name = Column(String(50))
    id_card_no = Column(String(18))
    id_card_front_url = Column(String(500))
    id_card_back_url = Column(String(500))
    credit_score = Column(Integer)
    credit_source = Column(String(50))
    education_level = Column(String(50))
    education_cert_url = Column(String(500))
    verify_status = Column(Enum("pending", "approved", "rejected"), default="pending")
    reject_reason = Column(String(500))
    verified_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("FlUser", back_populates="verifications")


class FlRole(Base):
    __tablename__ = "role"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    role_name = Column(String(50), nullable=False)
    role_code = Column(String(50), unique=True, nullable=False)
    description = Column(String(200))
    status = Column(Enum("active", "disabled"), default="active")
    created_at = Column(DateTime, default=datetime.utcnow)
    users = relationship("FlUserRole", back_populates="role")
    permissions = relationship("FlRolePermission", back_populates="role")


class FlPermission(Base):
    __tablename__ = "permission"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    permission_name = Column(String(100), nullable=False)
    permission_code = Column(String(100), unique=True, nullable=False)
    resource_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    roles = relationship("FlRolePermission", back_populates="permission")


class FlUserRole(Base):
    __tablename__ = "user_role"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("user.id"), nullable=False)
    role_id = Column(BigInteger, ForeignKey("role.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("FlUser", back_populates="roles")
    role = relationship("FlRole", back_populates="users")


class FlRolePermission(Base):
    __tablename__ = "role_permission"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    role_id = Column(BigInteger, ForeignKey("role.id"), nullable=False)
    permission_id = Column(BigInteger, ForeignKey("permission.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    role = relationship("FlRole", back_populates="permissions")
    permission = relationship("FlPermission", back_populates="roles")


# FlAuditLog已移至 app/models/fl_audit_log.py
