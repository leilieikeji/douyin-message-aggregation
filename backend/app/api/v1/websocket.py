"""WebSocket endpoint for real-time notifications"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, Query
import json
import logging
from app.security.websocket import manager
from app.security.auth import get_current_user, User

router = APIRouter()
logger = logging.getLogger("app")


@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    """WebSocket 实时消息推送"""
    await manager.connect(websocket, user_id)
    logger.info(f"User {user_id} connected via WebSocket")
    
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # 处理不同类型的消息
            if message.get("type") == "ping":
                await websocket.send_json({"type": "pong", "timestamp": str(datetime.now())})
            
            elif message.get("type") == "subscribe":
                # 订阅特定账户的消息
                logger.info(f"User {user_id} subscribed to {message.get('account_id')}")
                await websocket.send_json({
                    "type": "subscribed",
                    "account_id": message.get("account_id"),
                })
            
            elif message.get("type") == "unsubscribe":
                logger.info(f"User {user_id} unsubscribed from {message.get('account_id')}")
                await websocket.send_json({
                    "type": "unsubscribed",
                    "account_id": message.get("account_id"),
                })
    
    except WebSocketDisconnect:
        await manager.disconnect(websocket, user_id)
        logger.info(f"User {user_id} disconnected")
    except Exception as e:
        logger.error(f"WebSocket error for user {user_id}: {str(e)}")
        await manager.disconnect(websocket, user_id)


from datetime import datetime
