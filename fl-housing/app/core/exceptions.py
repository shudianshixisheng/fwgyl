from fastapi import HTTPException


class FlException(HTTPException):
    def __init__(self, message: str, code: int = 500):
        super().__init__(status_code=200, detail={"code": code, "message": message, "data": None})


class FlUnauthorized(FlException):
    def __init__(self, message: str = "未登录或Token失效"):
        super().__init__(message, 401)


class FlForbidden(FlException):
    def __init__(self, message: str = "无权限访问"):
        super().__init__(message, 403)


class FlNotFound(FlException):
    def __init__(self, message: str = "资源不存在"):
        super().__init__(message, 404)


class FlBadRequest(FlException):
    def __init__(self, message: str = "请求参数错误"):
        super().__init__(message, 400)
