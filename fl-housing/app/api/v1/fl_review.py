"""Day6: 点评API"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.response import fl_success
from app.core.dependencies import get_current_user, require_operator, require_developer, FlCurrentUser
from app.schemas.fl_talent_schema import FlReviewCreate, FlReviewReply, FlReviewAuditRequest
from app.services.fl_talent_service import fl_review_service

router = APIRouter(prefix="/review", tags=["点评管理"])


@router.post("/create")
def create_review(req: FlReviewCreate, user: FlCurrentUser = Depends(get_current_user), db: Session = Depends(get_db)):
    """发表点评"""
    return fl_success(fl_review_service.create_review(db, req, user.user_id), "发表成功，等待审核")


@router.get("/list")
def get_reviews(
    target_type: str = Query(...),
    target_id: int = Query(...),
    page: int = Query(1),
    page_size: int = Query(20),
    db: Session = Depends(get_db)
):
    """获取点评列表（公开）"""
    return fl_success(fl_review_service.get_reviews(db, target_type, target_id, page, page_size))


@router.post("/{review_id}/reply")
def reply_review(review_id: int, req: FlReviewReply, user: FlCurrentUser = Depends(require_developer), db: Session = Depends(get_db)):
    """[开发商]回复点评"""
    return fl_success(fl_review_service.reply_review(db, review_id, req, user.user_id), "回复成功")


@router.post("/{review_id}/audit")
def audit_review(review_id: int, req: FlReviewAuditRequest, user: FlCurrentUser = Depends(require_operator), db: Session = Depends(get_db)):
    """[运营]审核点评"""
    return fl_success(fl_review_service.audit_review(db, review_id, req), "审核完成")
