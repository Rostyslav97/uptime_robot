from datetime import timedelta

from config.settings.base import env

CELERY_BROKER_URL = env("REDIS_URL", default="redis://redis")
# CELERY_ACCEPT_CONTENT = ["json"]
# CELERY_TASK_SERIALIZER = ["json"]

CELERY_BEAT_SCHEDULE = {
    "generate_reports": {
        "task": "core.tasks.generate_reports",
        "schedule": timedelta(seconds=10),
    }
}