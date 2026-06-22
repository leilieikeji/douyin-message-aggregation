"""API Router - Main entry point for all API routes"""

from fastapi import APIRouter

from app.api.v1 import accounts, messages, analytics, auto_reply

api_router = APIRouter()

# Include routers
api_router.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])
api_router.include_router(messages.router, prefix="/messages", tags=["Messages"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(auto_reply.router, prefix="/auto-reply", tags=["Auto Reply"])
