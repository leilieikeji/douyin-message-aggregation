"""Message models for real-time sync"""

from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel


class MessageStatusEnum(str, Enum):
    unread = "unread"
    read = "read"
    replied = "replied"
    archived = "archived"


class MessageBase(BaseModel):
    account_id: str
    sender_id: str
    sender_name: str
    content: str
    status: MessageStatusEnum = MessageStatusEnum.unread


class MessageCreate(MessageBase):
    pass


class MessageUpdate(BaseModel):
    status: Optional[MessageStatusEnum] = None
    content: Optional[str] = None
    tags: Optional[list] = None


class MessageResponse(MessageBase):
    id: str
    created_at: datetime
    updated_at: datetime
    tags: list = []

    class Config:
        from_attributes = True


class MessageSync(BaseModel):
    """实时消息同步"""
    type: str  # new_message, update_message, delete_message
    data: MessageResponse
    timestamp: datetime
