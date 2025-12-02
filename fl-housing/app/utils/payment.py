"""
支付服务模块

【模拟状态】当前为模拟实现，所有支付均直接返回成功
【正式上线需开通】
  - 微信支付商户号及API密钥
  - 支付宝开放平台应用及密钥
  - 银联支付商户接入
  - 完成ICP备案和相关资质
"""
import uuid
from datetime import datetime


class FlPayment:
    def create_order(self, amount: float, order_no: str, description: str, pay_type: str = "wechat") -> dict:
        """
        创建支付订单
        【模拟】返回模拟的支付参数
        【正式】调用微信/支付宝API创建预支付订单
        """
        print(f"【模拟支付】创建订单: {order_no}, 金额: {amount}, 方式: {pay_type}")
        return {
            "order_no": order_no,
            "pay_type": pay_type,
            "amount": amount,
            "pay_url": f"https://mock-pay.example.com/pay?order={order_no}",  # 模拟支付链接
            "qr_code": f"mock://pay/{order_no}",  # 模拟二维码内容
            "expire_time": "2099-12-31 23:59:59"
        }
    
    def query_order(self, order_no: str, pay_type: str = "wechat") -> dict:
        """
        查询支付状态
        【模拟】始终返回支付成功
        【正式】调用微信/支付宝API查询订单状态
        """
        print(f"【模拟支付】查询订单: {order_no}")
        return {
            "order_no": order_no,
            "status": "paid",  # 模拟：始终返回已支付
            "paid_at": datetime.utcnow().isoformat(),
            "transaction_id": f"MOCK_{uuid.uuid4().hex[:16].upper()}"
        }
    
    def refund(self, order_no: str, amount: float, reason: str = "") -> dict:
        """
        申请退款
        【模拟】直接返回退款成功
        【正式】调用微信/支付宝API发起退款
        """
        print(f"【模拟支付】退款: {order_no}, 金额: {amount}, 原因: {reason}")
        return {
            "order_no": order_no,
            "refund_no": f"RF_{uuid.uuid4().hex[:12].upper()}",
            "status": "success",  # 模拟：直接成功
            "refund_at": datetime.utcnow().isoformat()
        }


fl_payment = FlPayment()
