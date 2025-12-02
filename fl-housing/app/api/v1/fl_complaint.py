"""Day6: 投诉API"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.response import fl_success
from app.core.dependencies import get_current_user, require_operator, FlCurrentUser
from app.schemas.fl_talent_schema import FlComplaintCreate, FlComplaintHandle, FlComplaintQuery
from app.services.fl_talent_service import fl_complaint_service

router = APIRouter(prefix="/complaint", tags=["投诉管理"])


@router.post("/create")
def create_complaint(req: FlComplaintCreate, user: FlCurrentUser = Depends(get_current_user), db: Session = Depends(get_db)):
    """提交投诉"""
    return fl_success(fl_complaint_service.create_complaint(db, req, user.user_id), "投诉提交成功")


@router.get("/{complaint_id}")
def get_complaint(complaint_id: int, user: FlCurrentUser = Depends(get_current_user), db: Session = Depends(get_db)):
    """获取投诉详情"""
    user_id = None if user.is_operator() else user.user_id
    return fl_success(fl_complaint_service.get_complaint(db, complaint_id, user_id))


@router.get("/list")
def get_complaint_list(
    page: int = Query(1),
    page_size: int = Query(20),
    complaint_type: str = Query(None),
    complaint_status: str = Query(None),
    target_type: str = Query(None),
    user: FlCurrentUser = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """投诉列表"""
    user_id = None if user.is_operator() else user.user_id
    return fl_success(fl_complaint_service.get_complaint_list(db, FlComplaintQuery(
        page=page, page_size=page_size, complaint_type=complaint_type,
        complaint_status=complaint_status, target_type=target_type
    ), user_id))


@router.post("/{complaint_id}/handle")
def handle_complaint(complaint_id: int, req: FlComplaintHandle, user: FlCurrentUser = Depends(require_operator), db: Session = Depends(get_db)):
    """[运营]处理投诉"""
    return fl_success(fl_complaint_service.handle_complaint(db, complaint_id, req, user.user_id, "运营人员"), "处理完成")
