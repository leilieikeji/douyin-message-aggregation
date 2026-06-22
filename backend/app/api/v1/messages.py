"""Messages API endpoints"""

from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()


@router.get("/")
async def list_messages(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    account_id: Optional[str] = None,
    status: Optional[str] = None,
):
    """获取消息列表"""
    return {"messages": [], "total": 0}


@router.get("/{message_id}")
async def get_message(message_id: str):
    """获取消息详情"""
    return {"message_id": message_id}


@router.post("/search")
async def search_messages(keyword: str, skip: int = 0, limit: int = 20):
    """搜索消息"""
    return {"results": [], "total": 0}


@router.post("/{message_id}/reply")
async def reply_message(message_id: str, content: str):
    """回复消息"""
    return {"message": "Reply sent"}
