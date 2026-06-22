"""Error handling middleware"""

from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("app")


async def error_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle exceptions"""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal Server Error",
            "path": str(request.url),
        },
    )
