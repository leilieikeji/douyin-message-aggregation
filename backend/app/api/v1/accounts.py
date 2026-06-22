"""Accounts API endpoints"""

from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List

router = APIRouter()


@router.post("/")
async def create_account():
    """创建新账户"""
    return {"message": "Account created"}


@router.get("/")
async def list_accounts(skip: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100)):
    """获取账户列表"""
    return {"accounts": [], "total": 0}


@router.get("/{account_id}")
async def get_account(account_id: str):
    """获取账户详情"""
    return {"account_id": account_id}


@router.put("/{account_id}")
async def update_account(account_id: str):
    """更新账户信息"""
    return {"message": "Account updated"}


@router.delete("/{account_id}")
async def delete_account(account_id: str):
    """删除账户"""
    return {"message": "Account deleted"}
