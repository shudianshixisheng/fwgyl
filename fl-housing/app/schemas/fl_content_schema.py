"""Day2: 内容Schema"""
from typing import Optional, List
from pydantic import BaseModel


class FlContentCreate(BaseModel):
    content_type: str
    title: str
    summary: Optional[str] = None
    content: str
    cover_image: Optional[str] = None
    images: Optional[List[str]] = None
    video_url: Optional[str] = None
    source: Optional[str] = None
    author: Optional[str] = None
    tags: Optional[List[str]] = None
    sort_order: int = 0


class FlContentUpdate(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    cover_image: Optional[str] = None
    images: Optional[List[str]] = None
    video_url: Optional[str] = None
    tags: Optional[List[str]] = None
    sort_order: Optional[int] = None
    status: Optional[str] = None


class FlContentQuery(BaseModel):
    page: int = 1
    page_size: int = 20
    content_type: Optional[str] = None
    keyword: Optional[str] = None
    status: Optional[str] = None


class FlBannerCreate(BaseModel):
    position: str
    title: Optional[str] = None
    image_url: str
    link_type: Optional[str] = "none"
    link_value: Optional[str] = None
    sort_order: int = 0


class FlBannerUpdate(BaseModel):
    title: Optional[str] = None
    image_url: Optional[str] = None
    link_type: Optional[str] = None
    link_value: Optional[str] = None
    sort_order: Optional[int] = None
    status: Optional[str] = None
