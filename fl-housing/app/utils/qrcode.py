"""
二维码生成模块

【说明】返回二维码内容URL，由前端生成二维码图片
"""
import uuid


def generate_house_qrcode(house_id: int, base_url: str = "https://lingshui.house") -> tuple:
    """
    生成房源好房码
    返回: (好房码编号, 扫码跳转URL)
    """
    code = f"HFC_{uuid.uuid4().hex[:10].upper()}"
    url = f"{base_url}/scan/house/{code}"
    return code, url


def generate_project_qrcode(project_id: int, base_url: str = "https://lingshui.house") -> tuple:
    """
    生成项目二维码
    返回: (项目码编号, 扫码跳转URL)
    """
    code = f"PRJ_{uuid.uuid4().hex[:10].upper()}"
    url = f"{base_url}/scan/project/{code}"
    return code, url
