"""Celery tasks configuration"""

from celery import Celery
from celery.schedules import crontab
from app.config import settings

celery_app = Celery(
    "douyin_aggregation",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

# 定时任务配置
celery_app.conf.beat_schedule = {
    "sync-messages-every-5-min": {
        "task": "app.tasks.sync.sync_messages_from_douyin",
        "schedule": crontab(minute="*/5"),
    },
    "process-auto-replies-every-minute": {
        "task": "app.tasks.sync.process_auto_replies",
        "schedule": crontab(minute="*"),
    },
    "generate-analytics-every-hour": {
        "task": "app.tasks.sync.generate_analytics_report",
        "schedule": crontab(minute=0),
    },
    "cleanup-old-messages-daily": {
        "task": "app.tasks.sync.cleanup_old_messages",
        "schedule": crontab(hour=2, minute=0),
    },
}
