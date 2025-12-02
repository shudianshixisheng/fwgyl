"""Day5: 定金托管Schema"""
from typing import Optional
from pydantic import BaseModel


class FlDepositTemplateCreate(BaseModel):
    template_name: str
    template_content: str
    deposit_amount: float
    lock_days: int = 7
    refund_rules: Optional[str] = None


class FlDepositTemplateUpdate(BaseModel):
    template_name: Optional[str] = None
    template_content: Optional[str] = None
    deposit_amount: Optional[float] = None
    lock_days: Optional[int] = None
    refund_rules: Optional[str] = None
    status: Optional[str] = None


class FlDepositOrderCreate(BaseModel):
    house_id: int
    template_id: Optional[int] = None
    buyer_name: str
    buyer_phone: str
    buyer_idcard: str
    deposit_amount: float
    pay_type: str = "wechat"


class FlDepositPayNotify(BaseModel):
    order_no: str
    transaction_id: str
    paid_amount: float
    pay_type: str


class FlDepositLockRequest(BaseModel):
    order_id: int
    action: str  # confirm / reject
    remark: Optional[str] = None


class FlDepositRefundRequest(BaseModel):
    order_id: int
    refund_reason: str


class FlDepositOrderQuery(BaseModel):
    page: int = 1
    page_size: int = 20
    order_no: Optional[str] = None
    buyer_phone: Optional[str] = None
    order_status: Optional[str] = None
    house_id: Optional[int] = None
    project_id: Optional[int] = None
