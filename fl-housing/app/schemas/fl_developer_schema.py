"""Day3: 开发商Schema"""
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class FlCompanyCreate(BaseModel):
    company_name: str
    unified_credit_code: str
    legal_person: str
    legal_person_phone: Optional[str] = None
    legal_person_idcard: Optional[str] = None
    company_type: str = "developer"
    registered_capital: Optional[float] = None
    established_date: Optional[datetime] = None
    business_scope: Optional[str] = None
    company_address: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    business_license_url: str
    developer_cert_url: Optional[str] = None
    developer_cert_level: Optional[str] = None


class FlCompanyUpdate(BaseModel):
    company_name: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    company_address: Optional[str] = None


class FlProjectCreate(BaseModel):
    project_name: str
    project_alias: Optional[str] = None
    project_address: str
    district: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    total_buildings: Optional[int] = None
    total_units: Optional[int] = None
    total_area: Optional[float] = None
    green_rate: Optional[float] = None
    volume_rate: Optional[float] = None
    parking_ratio: Optional[str] = None
    property_company: Optional[str] = None
    property_fee: Optional[float] = None
    presale_permit_no: Optional[str] = None
    presale_permit_url: Optional[str] = None
    delivery_standard: Optional[str] = None
    project_features: Optional[List[str]] = None
    cover_image: Optional[str] = None
    images: Optional[List[str]] = None
    video_url: Optional[str] = None
    vr_url: Optional[str] = None


class FlProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    project_alias: Optional[str] = None
    project_address: Optional[str] = None
    cover_image: Optional[str] = None
    images: Optional[List[str]] = None
    video_url: Optional[str] = None
    vr_url: Optional[str] = None
    project_features: Optional[List[str]] = None
    is_recommend: Optional[bool] = None
    sort_order: Optional[int] = None


class FlProjectQuery(BaseModel):
    page: int = 1
    page_size: int = 20
    keyword: Optional[str] = None
    district: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    audit_status: Optional[str] = None


class FlAuditRequest(BaseModel):
    audit_status: str
    audit_remark: Optional[str] = None
