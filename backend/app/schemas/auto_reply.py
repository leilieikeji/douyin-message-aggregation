"""Auto-reply rules and processing"""

from datetime import datetime
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel


class RuleTriggerType(str, Enum):
    keyword = "keyword"
    regex = "regex"
    sender = "sender"
    time = "time"


class AutoReplyRuleBase(BaseModel):
    name: str
    description: Optional[str] = None
    trigger_type: RuleTriggerType
    trigger_value: str
    response_template: str
    account_ids: List[str]
    enabled: bool = True
    priority: int = 0


class AutoReplyRuleCreate(AutoReplyRuleBase):
    pass


class AutoReplyRuleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    trigger_value: Optional[str] = None
    response_template: Optional[str] = None
    enabled: Optional[bool] = None
    priority: Optional[int] = None


class AutoReplyRuleResponse(AutoReplyRuleBase):
    id: str
    created_at: datetime
    updated_at: datetime
    trigger_count: int = 0
    last_triggered: Optional[datetime] = None

    class Config:
        from_attributes = True
