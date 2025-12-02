"""Day4: 房源Schema"""
from typing import Optional, List
from pydantic import BaseModel


class FlHouseCreate(BaseModel):
    project_id: int
    building_no: str
    unit_no: Optional[str] = None
    floor_no: int
    room_no: str
    house_type: str = "apartment"
    bedroom_count: int
    living_room_count: int = 1
    bathroom_count: int = 1
    kitchen_count: int = 1
    balcony_count: int = 0
    orientation: Optional[str] = None
    building_area: float
    inside_area: Optional[float] = None
    total_price: float
    unit_price: float
    decoration: str = "rough"
    property_type: str = "residential"
    property_years: int = 70
    floor_plan_url: Optional[str] = None
    images: Optional[List[str]] = None
    video_url: Optional[str] = None
    vr_url: Optional[str] = None
    is_real_house: bool = True
    is_current_house: bool = False
    can_view: bool = True


class FlHouseUpdate(BaseModel):
    total_price: Optional[float] = None
    unit_price: Optional[float] = None
    floor_plan_url: Optional[str] = None
    images: Optional[List[str]] = None
    video_url: Optional[str] = None
    vr_url: Optional[str] = None
    sale_status: Optional[str] = None
    is_recommend: Optional[bool] = None
    sort_order: Optional[int] = None
    status: Optional[str] = None


class FlHouseQuery(BaseModel):
    page: int = 1
    page_size: int = 20
    project_id: Optional[int] = None
    keyword: Optional[str] = None
    house_type: Optional[str] = None
    bedroom_count: Optional[int] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    min_area: Optional[float] = None
    max_area: Optional[float] = None
    decoration: Optional[str] = None
    orientation: Optional[str] = None
    sale_status: Optional[str] = None
    is_current_house: Optional[bool] = None
    sort_by: Optional[str] = None
    sort_order: Optional[str] = "desc"
