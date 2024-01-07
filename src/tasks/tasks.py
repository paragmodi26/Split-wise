"""
Celery worker tasks definition
"""
from celery.schedules import crontab
from src.tasks.celery import celery_master_app

celery_master_app.autodiscover_tasks()
celery_master_app.conf.timezone = "UTC"

celery_master_app.conf.beat_schedule = {
    # DECISION
#     "task_decision_fill_up_reminder": {
#         "task": "celery_tasks.workers.main.task_decision_fill_up_reminder",
#         "schedule": crontab(hour='*/1', minute=0),
#     },
    #     "task_decision_recommendation_reminder": {
    #         "task": "celery_tasks.workers.main.task_decision_recommendation_reminder",
    #         "schedule": crontab(hour='*/1', minute=0),
    #     },
    #     "task_decision_recommended_review_reminder": {
    #         "task": "celery_tasks.workers.main.task_decision_recommended_review_reminder",
    #         "schedule": crontab(hour='*/1', minute=0),
    #     },
    # MEETING AGENDA
#     "task_agenda_summary": {
#         "task": "celery_tasks.workers.main.task_agenda_summary",
#         "schedule": crontab(hour='4,8,12,16', minute='30'),
#     },
    # MEETING VOTING
#     "task_pre_discussion_voting_reminder_summary": {
#         "task": "celery_tasks.workers.main.task_pre_discussion_voting_reminder_summary",
#         "schedule": crontab(hour='6,10,14', minute='30'),
#     },
#     "task_pre_discussion_voting_reminder_final_india": {
#         "task": "celery_tasks.workers.main.task_pre_discussion_voting_reminder_final_india",
#         "schedule": crontab(hour='0', minute='45'),
#     },
#     "task_pre_discussion_voting_reminder_final_mena": {
#         "task": "celery_tasks.workers.main.task_pre_discussion_voting_reminder_final_mena",
#         "schedule": crontab(hour='0', minute='45'),
#     },
#     "task_pre_discussion_voting_reminder_final_sea": {
#         "task": "celery_tasks.workers.main.task_pre_discussion_voting_reminder_final_sea",
#         "schedule": crontab(hour='4', minute='15'),
#     },
#     "task_post_discussion_voting_reminder_final_india": {
#         "task": "celery_tasks.workers.main.task_post_discussion_voting_reminder_final_india",
#         "schedule": crontab(hour='11', minute='15'),
#     },
#     "task_post_discussion_voting_reminder_final_mena": {
#         "task": "celery_tasks.workers.main.task_post_discussion_voting_reminder_final_mena",
#         "schedule": crontab(hour='11', minute='15'),
#     },
#     "task_post_discussion_voting_reminder_final_sea": {
#         "task": "celery_tasks.workers.main.task_post_discussion_voting_reminder_final_sea",
#         "schedule": crontab(hour='9', minute='15'),
#     },
#     "task_pre_discussion_voting_summary_sea": {
#         "task": "celery_tasks.workers.main.task_pre_discussion_voting_summary_sea",
#         "schedule": crontab(hour='5', minute='0'),
#     },
#     "task_pre_discussion_voting_summary_india": {
#         "task": "celery_tasks.workers.main.task_pre_discussion_voting_summary_india",
#         "schedule": crontab(hour='1', minute='30'),
#     },
#     "task_pre_discussion_voting_summary_mena": {
#         "task": "celery_tasks.workers.main.task_pre_discussion_voting_summary_mena",
#         "schedule": crontab(hour='1', minute='30'),
#     },
#     "task_final_voting_summary": {
#         "task": "celery_tasks.workers.main.task_final_voting_summary",
#         "schedule": crontab(hour='11', minute='30'),
#     },
    # NOTES REMINDER
    "task_reminder_notes": {
        "task": "celery_tasks.workers.main.task_reminder_notes",
        "schedule": crontab(hour='4', minute='30'),
    },
    # NOTIFICATION
    "task_delete_old_notification": {
        "task": "celery_tasks.workers.main.task_delete_old_notification",
        "schedule": crontab(hour='*/8', minute=0),
    },
#     "task_save_agenda_notification": {
#         "task": "celery_tasks.workers.main.task_save_agenda_notification",
#         "schedule": crontab(minute='*/2'),
#     },
#     "task_decision_recommended_notification": {
#         "task": "celery_tasks.workers.main.task_decision_recommended_notification",
#         "schedule": crontab(minute='*/2'),
#     },
    "task_notes_tag_notification": {
        "task": "celery_tasks.workers.main.task_notes_tag_notification",
        "schedule": crontab(minute='*/2'),
    },
    "task_notes_reply_notification": {
        "task": "celery_tasks.workers.main.task_notes_reply_notification",
        "schedule": crontab(minute='*/2'),
    },
#     "task_finance_manager_email": {
#         "task": "celery_tasks.workers.main.task_finance_manager_email",
#         "schedule": crontab(minute='*/2'),
#     },
#     "task_partner_email": {
#         "task": "celery_tasks.workers.main.task_partner_email",
#         "schedule": crontab(minute='*/2'),
#     },
    # Generate Agenda
    "task_generate_agenda": {
        "task": "celery_tasks.workers.main.task_generate_agenda",
        "schedule": crontab(minute='*/5'),
    },
    # Get Real
#     "task_get_real_weekly_updates": {
#         "task": "celery_tasks.workers.main.task_get_real_weekly_updates",
#         "schedule": crontab(hour='22', minute='40',day_of_week='sun'),
#     },
#     "task_get_real_120_days_no_update": {
#         "task": "celery_tasks.workers.main.task_get_real_120_days_no_update",
#         "schedule": crontab(hour='11', minute='30', day_of_week='fri'),
#     },
    # Who2 Notes
#     "task_who2_notes": {
#         "task": "celery_tasks.workers.main.task_who2_notes",
#         "schedule": crontab(minute='*/10'),
#     },
#     "task_who2_sync_full_company_notes": {
#         "task": "celery_tasks.workers.main.task_who2_sync_full_company_notes",
#         "schedule": crontab(minute='*/30'),
#     },
#     "task_delete_attachment_from_s3": {
#         "task": "celery_tasks.workers.main.task_delete_attachment_from_s3",
#         "schedule": crontab(minute='*/23'),
#     },
#     "task_new_portfolio_company_reminder": {
#         "task": "celery_tasks.workers.main.task_new_portfolio_company_reminder",
#         "schedule": crontab(hour='03', minute='30'),
#     },
#     "task_small_ic_company_notification": {
#         "task": "celery_tasks.workers.main.task_small_ic_company_notification",
#         "schedule": crontab(minute='*/2'),
#     },
#     "task_gt_send_final_docs": {
#         "task": "celery_tasks.workers.main.task_gt_send_final_docs",
#         "schedule": crontab(minute='*/2'),
#     },
    "task_event_based_task": {
        "task": "celery_tasks.workers.main.task_event_based_task",
        "schedule": crontab(minute='*/1'),
    },
    "task_delete_old_search_logs_index": {
        "task": "celery_tasks.workers.main.task_delete_old_search_logs_index",
        "schedule": crontab(day_of_month='10'),
    },
#     "task_get_real_notes_sentiment": {
#         "task": "celery_tasks.workers.main.task_get_real_notes_sentiment",
#         "schedule": crontab(minute='*/5'),
#     },
}
