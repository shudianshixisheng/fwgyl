from typing import Any


def fl_success(data: Any = None, message: str = "success") -> dict:
    return {"code": 200, "message": message, "data": data}


def fl_error(message: str, code: int = 500) -> dict:
    return {"code": code, "message": message, "data": None}


def fl_page(items: list, total: int, page: int, page_size: int) -> dict:
    total_pages = (total + page_size - 1) // page_size
    return fl_success({"list": items, "total": total, "page": page, "page_size": page_size, "total_pages": total_pages})
