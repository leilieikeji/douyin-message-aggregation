"""Auto Reply API endpoints"""

from fastapi import APIRouter, Query

router = APIRouter()


@router.post("/rules")
async def create_rule():
    """创建自动回复规则"""
    return {"message": "Rule created"}


@router.get("/rules")
async def list_rules(skip: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100)):
    """获取规则列表"""
    return {"rules": [], "total": 0}


@router.get("/rules/{rule_id}")
async def get_rule(rule_id: str):
    """获取规则详情"""
    return {"rule_id": rule_id}


@router.put("/rules/{rule_id}")
async def update_rule(rule_id: str):
    """更新规则"""
    return {"message": "Rule updated"}


@router.delete("/rules/{rule_id}")
async def delete_rule(rule_id: str):
    """删除规则"""
    return {"message": "Rule deleted"}
