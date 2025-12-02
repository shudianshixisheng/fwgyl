from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sys
sys.path.append(".")
from config import settings

# SQLite不支持pool_pre_ping
connect_args = {}
if settings.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
    engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG, connect_args=connect_args)
else:
    engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def init_db():
    """初始化数据库表"""
    Base.metadata.create_all(bind=engine)
    # 初始化管理员账号
    _init_admin()

def _init_admin():
    """初始化管理员账号：admin / 13888888888 / 123456"""
    from app.models.fl_user import FlUser, FlRole, FlUserRole
    from app.core.security import fl_security
    
    db = SessionLocal()
    try:
        # 检查管理员是否已存在
        admin = db.query(FlUser).filter(FlUser.username == "admin").first()
        if admin:
            return
        
        # 创建管理员账号
        admin = FlUser(
            phone="13888888888",
            username="admin",
            password_hash=fl_security.hash_password("123456"),
            nickname="超级管理员",
            user_level="verified",
            status="active"
        )
        db.add(admin)
        db.flush()
        
        # 分配管理员角色
        admin_role = db.query(FlRole).filter(FlRole.role_code == "ROLE_ADMIN").first()
        if admin_role:
            db.add(FlUserRole(user_id=admin.id, role_id=admin_role.id))
        
        db.commit()
        print("【初始化】管理员账号创建成功: admin / 13888888888 / 123456")
    except Exception as e:
        db.rollback()
        print(f"【初始化】管理员账号已存在或创建失败: {e}")
    finally:
        db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
