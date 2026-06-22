"""Analytics API endpoints"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/summary")
async def get_summary():
    """获取统计摘要"""
    return {
        "total_messages": 0,
        "total_accounts": 0,
        "unread_count": 0,
        "reply_count": 0,
    }


@router.get("/messages/trends")
async def get_message_trends(days: int = 7):
    """消息趋势分析"""
    return {"trends": []}


@router.get("/accounts/stats")
async def get_account_stats():
    """账户统计信息"""
    return {"stats": []}
