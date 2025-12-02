"""
短信服务模块

=============================================================================
【当前状态】测试模拟模式
  - 验证码打印到控制台，不会真实发送短信
  - 万能验证码: 666666 (任何手机号都可通过)
  
【正式上线】需要企业资质开通阿里云短信API，步骤如下:
  1. 注册阿里云账号并完成企业实名认证: https://www.aliyun.com
  2. 开通短信服务: 控制台搜索"短信服务"并开通
  3. 申请短信签名: 如"陵水住房"（需1-2天审核）
  4. 申请短信模板: 如"您的验证码是${code}，5分钟内有效"
  5. 获取AccessKey: 控制台右上角 -> AccessKey管理 -> 创建
  6. 安装SDK: pip install alibabacloud_dysmsapi20170525
  7. 配置下方 ALIYUN_SMS_CONFIG 并取消注释真实发送代码
  
【真实短信代码位置】本文件第70-95行（已注释）
=============================================================================
"""
import random
from datetime import datetime, timedelta

# 内存存储验证码（生产环境建议使用Redis）
sms_codes: dict = {}

# =============================================================================
# 阿里云短信配置（正式上线时填写）
# =============================================================================
ALIYUN_SMS_CONFIG = {
    "access_key_id": "your_access_key_id",         # 阿里云AccessKey ID
    "access_key_secret": "your_access_key_secret", # 阿里云AccessKey Secret
    "sign_name": "陵水住房",                         # 短信签名（需审核通过）
    "template_code": "SMS_123456789",              # 短信模板CODE（需审核通过）
}

# =============================================================================
# 阿里云短信SDK（正式上线时取消注释并安装: pip install alibabacloud_dysmsapi20170525）
# =============================================================================
# from alibabacloud_dysmsapi20170525.client import Client as DysmsapiClient
# from alibabacloud_dysmsapi20170525 import models as dysmsapi_models
# from alibabacloud_tea_openapi import models as open_api_models
# 
# def create_aliyun_sms_client():
#     """创建阿里云短信客户端"""
#     config = open_api_models.Config(
#         access_key_id=ALIYUN_SMS_CONFIG["access_key_id"],
#         access_key_secret=ALIYUN_SMS_CONFIG["access_key_secret"]
#     )
#     config.endpoint = "dysmsapi.aliyuncs.com"
#     return DysmsapiClient(config)


class FlSms:
    def generate_code(self, length: int = 6) -> str:
        """生成随机验证码"""
        return "".join([str(random.randint(0, 9)) for _ in range(length)])
    
    def send(self, phone: str, code: str) -> bool:
        """
        发送短信验证码
        
        【当前】测试模式，验证码打印到控制台
        【正式】取消注释下方阿里云发送代码
        """
        # 存储验证码，5分钟有效
        sms_codes[phone] = {
            "code": code,
            "exp": datetime.utcnow() + timedelta(minutes=5)
        }
        
        # =========================================
        # 【测试模式】模拟发送，打印到控制台
        # =========================================
        print(f"【模拟短信】手机号: {phone}, 验证码: {code}, 5分钟有效")
        return True
        
        # =========================================
        # 【正式模式】阿里云短信发送（取消注释启用）
        # =========================================
        # try:
        #     client = create_aliyun_sms_client()
        #     send_request = dysmsapi_models.SendSmsRequest(
        #         phone_numbers=phone,
        #         sign_name=ALIYUN_SMS_CONFIG["sign_name"],
        #         template_code=ALIYUN_SMS_CONFIG["template_code"],
        #         template_param='{"code":"' + code + '"}'
        #     )
        #     response = client.send_sms(send_request)
        #     if response.body.code == "OK":
        #         print(f"【阿里云短信】发送成功: {phone}")
        #         return True
        #     else:
        #         print(f"【阿里云短信】发送失败: {response.body.message}")
        #         return False
        # except Exception as e:
        #     print(f"【阿里云短信】发送异常: {str(e)}")
        #     return False
    
    def verify(self, phone: str, code: str) -> bool:
        """
        验证短信验证码
        
        【测试模式】万能验证码 666666 始终通过
        【正式模式】删除万能验证码逻辑
        """
        # =========================================
        # 【测试模式】万能验证码（正式上线请删除此段）
        # =========================================
        if code == "666666":
            return True
        
        # =========================================
        # 正常验证逻辑
        # =========================================
        stored = sms_codes.get(phone)
        if not stored:
            return False
        if stored["exp"] < datetime.utcnow():
            del sms_codes[phone]
            return False
        if stored["code"] != code:
            return False
        del sms_codes[phone]
        return True


fl_sms = FlSms()
