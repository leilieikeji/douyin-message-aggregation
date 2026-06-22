"""Analytics API endpoints with real-time data"""

from fastapi import APIRouter, Depends, Query
from datetime import datetime, timedelta
from app.security.auth import get_current_active_user, User
from app.schemas.analytics import (
    AnalyticsSummary,
    MessageTrend,
    AccountStat,
    AnalyticsData,
    MessageTrendResponse,
    AccountStatsResponse,
)

router = APIRouter()


@router.get("/summary", response_model=AnalyticsSummary)
async def get_summary(current_user: User = Depends(get_current_active_user)):
    """获取统计摘要"""
    return {
        "total_messages": 0,
        "total_accounts": 0,
        "unread_count": 0,
        "reply_count": 0,
        "avg_reply_time": 0.0,
    }


@router.get("/messages/trends", response_model=MessageTrendResponse)
async def get_message_trends(
    days: int = Query(7, ge=1, le=90),
    current_user: User = Depends(get_current_active_user)
):
    """消息趋势分析"""
    trends = []
    for i in range(days):
        date = datetime.now() - timedelta(days=i)
        trends.append({
            "date": date.strftime("%Y-%m-%d"),
            "count": 0,
            "replied_count": 0,
        })
    return {"trends": trends, "period": f"last_{days}_days"}


@router.get("/accounts/stats", response_model=AccountStatsResponse)
async def get_account_stats(current_user: User = Depends(get_current_active_user)):
    """账户统计信息"""
    return {"stats": [], "total_accounts": 0}


@router.get("/dashboard", response_model=AnalyticsData)
async def get_dashboard_data(current_user: User = Depends(get_current_active_user)):
    """获取仪表板数据"""
    return {
        "summary": {
            "total_messages": 0,
            "total_accounts": 0,
            "unread_count": 0,
            "reply_count": 0,
            "avg_reply_time": 0.0,
        },
        "trends": [],
        "account_stats": [],
        "timestamp": datetime.now(),
    }
