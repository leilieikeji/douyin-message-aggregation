"""Analytics models"""

from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel


class AnalyticsSummary(BaseModel):
    total_messages: int
    total_accounts: int
    unread_count: int
    reply_count: int
    avg_reply_time: float


class MessageTrend(BaseModel):
    date: str
    count: int
    replied_count: int


class MessageTrendResponse(BaseModel):
    trends: List[MessageTrend]
    period: str


class AccountStat(BaseModel):
    account_id: str
    account_name: str
    message_count: int
    reply_count: int
    reply_rate: float
    avg_reply_time: float


class AccountStatsResponse(BaseModel):
    stats: List[AccountStat]
    total_accounts: int


class AnalyticsData(BaseModel):
    summary: AnalyticsSummary
    trends: List[MessageTrend]
    account_stats: List[AccountStat]
    timestamp: datetime
