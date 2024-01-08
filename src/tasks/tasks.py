"""
Celery worker tasks definition
"""
from celery.schedules import crontab
from src.tasks.celery import celery_master_app

celery_master_app.autodiscover_tasks()
celery_master_app.conf.timezone = "IST"

celery_master_app.conf.beat_schedule = {
    
    "split_amount_weekly_task": {
        "task": "celery_tasks.workers.main.split_amount_weekly_task",
        "schedule": crontab(hour='23', minute='59',day_of_week='mon'),
    },
    
}
