"""Updated main application with new features"""

from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.config import settings
from app.api import router
from app.api.v1 import auth, websocket
from app.middleware.error_handler import error_exception_handler
from app.utils.logger import setup_logging

# Setup logging
logger = setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events"""
    # Startup
    logger.info("✅ Application starting up...")
    logger.info(f"DEBUG mode: {settings.DEBUG}")
    logger.info(f"Database: {settings.MONGODB_URL}")
    logger.info(f"Redis: {settings.REDIS_URL}")
    
    yield
    
    # Shutdown
    logger.info("🛑 Application shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    description="抖音私信聚合系统 - Douyin Private Message Aggregation System",
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors(),
            "body": exc.body
        },
    )


# Include routers
app.include_router(router.api_router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(websocket.router, tags=["WebSocket"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": f"欢迎使用 {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "openapi_schema": "/openapi.json",
        "features": [
            "User Authentication",
            "Real-time Message Sync",
            "WebSocket Notifications",
            "Analytics Dashboard",
            "Auto-reply Engine",
        ],
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "timestamp": str(logging.datetime.datetime.now()),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
