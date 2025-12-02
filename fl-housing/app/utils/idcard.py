"""
身份证二要素认证模块

【当前状态】测试模拟，直接返回验证通过
【正式上线】需开通阿里云/腾讯云 身份证二要素认证API
【真实代码位置】本文件第60-100行（已注释）
"""
# ===========================================
# 阿里云身份证二要素认证 配置
# 申请地址：https://market.aliyun.com/products/57000002/cmapi025518.html
# ===========================================
# ALIYUN_IDCARD_APP_CODE = "your_app_code_here"
# ALIYUN_IDCARD_API_URL = "https://idenauthen.market.alicloudapi.com/idenAuthentication"


class FlIdcard:
    def verify_two_elements(self, real_name: str, id_card_no: str) -> dict:
        """
        身份证二要素验证（姓名+身份证号）
        【模拟】直接返回验证通过
        【正式】调用阿里云/腾讯云实名认证API
        """
        print(f"【模拟实名】二要素验证: {real_name}, {id_card_no[:6]}****{id_card_no[-4:]}")
        # 模拟：基本格式校验
        if len(id_card_no) != 18:
            return {"success": False, "message": "身份证号格式错误"}
        if len(real_name) < 2:
            return {"success": False, "message": "姓名格式错误"}
        # 模拟：返回成功
        return {
            "success": True,
            "message": "验证通过",
            "data": {
                "name": real_name,
                "id_card": f"{id_card_no[:6]}********{id_card_no[-4:]}",
                "gender": "男" if int(id_card_no[-2]) % 2 == 1 else "女",
                "birth_date": f"{id_card_no[6:10]}-{id_card_no[10:12]}-{id_card_no[12:14]}"
            }
        }
    
    def verify_three_elements(self, real_name: str, id_card_no: str, phone: str) -> dict:
        """
        身份证三要素验证（姓名+身份证号+手机号）
        【模拟】直接返回验证通过
        【正式】调用运营商三要素验证API
        """
        print(f"【模拟实名】三要素验证: {real_name}, {id_card_no[:6]}****, {phone[:3]}****{phone[-4:]}")
        two_result = self.verify_two_elements(real_name, id_card_no)
        if not two_result["success"]:
            return two_result
        # 模拟：手机号格式校验
        if len(phone) != 11 or not phone.startswith("1"):
            return {"success": False, "message": "手机号格式错误"}
        return {
            "success": True,
            "message": "验证通过",
            "data": two_result["data"]
        }


fl_idcard = FlIdcard()


# ===========================================
# 【真实代码】阿里云身份证二要素认证API调用
# 正式上线时取消注释并配置APP_CODE
# ===========================================
# import requests
# 
# def verify_two_elements_real(real_name: str, id_card_no: str) -> dict:
#     """
#     阿里云身份证二要素认证（姓名+身份证号）
#     API文档：https://market.aliyun.com/products/57000002/cmapi025518.html
#     """
#     url = ALIYUN_IDCARD_API_URL
#     headers = {
#         "Authorization": f"APPCODE {ALIYUN_IDCARD_APP_CODE}",
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     data = {
#         "name": real_name,
#         "idNo": id_card_no
#     }
#     try:
#         response = requests.post(url, headers=headers, data=data, timeout=10)
#         result = response.json()
#         # respCode=0000 表示验证通过
#         if result.get("respCode") == "0000":
#             return {"success": True, "message": "验证通过", "data": result}
#         else:
#             return {"success": False, "message": result.get("respMessage", "验证失败")}
#     except Exception as e:
#         return {"success": False, "message": f"API调用失败: {str(e)}"}
