"""Day6: 人才/点评/投诉Schema"""
from typing import Optional, List
from pydantic import BaseModel
from datetime import date


class FlTalentApplicationCreate(BaseModel):
    talent_type: str
    real_name: str
    id_card_no: str
    phone: str
    gender: Optional[str] = None
    birth_date: Optional[date] = None
    education: str
    graduation_school: Optional[str] = None
    graduation_date: Optional[date] = None
    major: Optional[str] = None
    work_unit: Optional[str] = None
    work_position: Optional[str] = None
    work_years: Optional[int] = None
    professional_title: Optional[str] = None
    talent_cert_no: Optional[str] = None
    id_card_front_url: str
    id_card_back_url: str
    education_cert_url: str
    degree_cert_url: Optional[str] = None
    talent_cert_url: Optional[str] = None
    other_cert_urls: Optional[List[str]] = None


class FlTalentAuditRequest(BaseModel):
    application_status: str
    reject_reason: Optional[str] = None
    discount_rate: Optional[float] = None
    subsidy_amount: Optional[float] = None


class FlReviewCreate(BaseModel):
    target_type: str
    target_id: int
    rating: int
    content: Optional[str] = None
    images: Optional[List[str]] = None
    is_anonymous: int = 0


class FlReviewReply(BaseModel):
    reply_content: str


class FlReviewAuditRequest(BaseModel):
    status: str
    reject_reason: Optional[str] = None


class FlComplaintCreate(BaseModel):
    complaint_type: str
    target_type: str
    target_id: int
    title: str
    content: str
    images: Optional[List[str]] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None


class FlComplaintHandle(BaseModel):
    complaint_status: str
    handle_result: Optional[str] = None


class FlComplaintQuery(BaseModel):
    page: int = 1
    page_size: int = 20
    complaint_type: Optional[str] = None
    complaint_status: Optional[str] = None
    target_type: Optional[str] = None
