"""Day1: 审计日志API"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.response import fl_success
from app.core.dependencies import require_admin, FlCurrentUser
from app.services.fl_audit_log_service import fl_audit_log_service

router = APIRouter(prefix="/admin/audit", tags=["审计管理"])


@router.get("/logs")
def get_audit_logs(
    page: int = Query(1, description="页码"),
    page_size: int = Query(20, description="每页数量"),
    module: str = Query(None, description="操作模块筛选"),
    username: str = Query(None, description="用户名/ID模糊搜索"),
    start_date: str = Query(None, description="开始日期 YYYY-MM-DD"),
    end_date: str = Query(None, description="结束日期 YYYY-MM-DD"),
    user: FlCurrentUser = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """
    [管理员] 查询操作日志
    - 支持分页
    - 支持按模块筛选
    - 支持按用户名模糊搜索
    - 支持按日期范围筛选
    """
    try:
        result = fl_audit_log_service.get_log_list(
            db, page, page_size, module, username, start_date, end_date
        )
        return fl_success(result)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"code": 500, "message": str(e), "data": None}


@router.get("/modules")
def get_audit_modules(user: FlCurrentUser = Depends(require_admin)):
    """[管理员] 获取所有操作模块列表"""
    modules = list(fl_audit_log_service.MODULE_MAP.values())
    return fl_success({"modules": modules})
