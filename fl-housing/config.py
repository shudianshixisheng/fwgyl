import os

class Settings:
    APP_NAME = "fl-housing"
    DEBUG = True
    API_V1_PREFIX = "/api/v1"
    # MySQL配置（请修改密码）:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:123456@localhost:3306/lingshui_housing")
    # SQLite备用: DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./fl_housing.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "fl-housing-secret-key")
    TOKEN_EXPIRE_DAYS = 30
    UPLOAD_DIR = "./uploads"
    MAX_UPLOAD_SIZE = 50 * 1024 * 1024

settings = Settings()
