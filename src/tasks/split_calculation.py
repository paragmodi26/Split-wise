"""task file for celery"""
import asyncio
import copy
import logging
from src.db.session import clear_db_session, SessionLocal
from src.services.amount_split.model import AmountSplitModel
from src.services.group.model import GroupModel
from src.services.user.model import UserModel
from src.tasks.celery import celery_master_app, is_duplicate_task
from src.utils.common import EmailInBound
from src.utils.email import Email
from src.utils.email_template import SplitBillNotificationTemplate

db = SessionLocal()


async def split_amount_task(_id: int):
    """task for sample"""
    try:
        split_data = AmountSplitModel.get_by_id(_id=_id)
        if split_data:
            group_data = GroupModel.get_by_id(_id=split_data.group_id)
            user_ids = group_data.user_ids if group_data else []
            user_data = UserModel.get_user(ids=user_ids) if user_ids else []
            user_dict = {}
            for user in user_data:
                user_dict[user.id] = user
            temp_dict = {}
            new_count = 0
            for relative_data in split_data.relative_meta or []:
                temp_dict[relative_data.get("user_id")] = relative_data.get("member_count")
                new_count += relative_data.get("member_count", 0)
            total_amount = split_data.amount
            number_of_users = len(user_ids) + new_count
            per_user_share = round((total_amount/number_of_users), 2) if number_of_users and total_amount else 0
            email_dict = {}
            payed_user_id = split_data.user_id
            payed_user_data = user_dict.get(payed_user_id)
            payed_user_dict = {"pay": {}, "take": {}}
            for key, user_data in user_dict.items():
                if key != int(payed_user_id):
                    number_ = 0
                    if key in temp_dict:
                        number_ = temp_dict[key]
                    amount = per_user_share + (per_user_share * number_)
                    if amount:
                        message = f"""{user_data.name}, you have to pay {amount}/- in the group name "{group_data.group_name}" """
                        message += f"""for the expense {group_data.expense_name}.""" if group_data.expense_name else " for the new expense."
                        message += f"""done by {payed_user_data.name}"""
                        email_dict[user_data.email] = message

                    meta_data = copy.deepcopy(user_data.meta_data) if user_data.meta_data else {}
                    group_meta_data = copy.deepcopy(meta_data[str(split_data.group_id)]) if meta_data and str(split_data.group_id) in meta_data else {}
                    payed_user_id = str(payed_user_id)
                    key = str(key)
                    if "pay" not in group_meta_data and "take" not in group_meta_data:
                        group_meta_data["pay"] = {payed_user_id: amount}

                    elif "pay" in group_meta_data and group_meta_data["pay"]:
                        if payed_user_id not in group_meta_data["pay"]:
                            if payed_user_id in group_meta_data.get("take", {}):
                                take_amount = group_meta_data.get("take", {}).get(payed_user_id)
                                if take_amount > amount:
                                    group_meta_data["take"][payed_user_id] = take_amount - amount
                                elif take_amount == amount:
                                    _ = group_meta_data["take"].pop(payed_user_id) if payed_user_id in group_meta_data["take"] else None
                                    _ = group_meta_data["pay"].pop(payed_user_id) if payed_user_id in group_meta_data["pay"] else None
                                else:
                                    _ = group_meta_data["take"].pop(payed_user_id) if payed_user_id in group_meta_data["take"] else None
                                    group_meta_data["pay"][payed_user_id] = amount - take_amount
                            else:
                                group_meta_data["pay"] = group_meta_data["pay"] | {payed_user_id: amount}
                        else:
                            group_meta_data["pay"][payed_user_id] = (group_meta_data["pay"][payed_user_id] or 0) + amount

                    elif "take" in group_meta_data and group_meta_data["take"]:
                        take_amount = group_meta_data["take"].get(payed_user_id)
                        if "pay" not in group_meta_data:
                            group_meta_data["pay"] = {}
                        if take_amount and take_amount > amount:
                            group_meta_data["take"][payed_user_id] = take_amount - amount
                        elif take_amount and take_amount < amount:
                            group_meta_data["pay"][payed_user_id] = amount - take_amount
                            del group_meta_data["take"][payed_user_id]
                        elif take_amount and take_amount == amount:
                            _ = group_meta_data["take"].pop(payed_user_id) if payed_user_id in group_meta_data["take"] else None
                            _ = group_meta_data["pay"].pop(payed_user_id) if payed_user_id in group_meta_data["pay"] else None
                        else:
                            group_meta_data["pay"][payed_user_id] = amount
                            if payed_user_id in group_meta_data["take"]:
                                del group_meta_data["take"][payed_user_id]
                    if group_meta_data:
                        if payed_user_id in group_meta_data["pay"]:
                            payed_user_dict["take"][key] = group_meta_data["pay"][payed_user_id]
                        elif payed_user_id in group_meta_data["take"]:
                            payed_user_dict["pay"][key] = group_meta_data["take"][payed_user_id]
                        meta_data[str(split_data.group_id)] = group_meta_data
                        UserModel.patch(_id=int(key), **{"meta_data": meta_data})

            meta_data = copy.deepcopy(payed_user_data.meta_data) if payed_user_data.meta_data else {}
            meta_data[str(split_data.group_id)] = payed_user_dict
            UserModel.patch(_id=int(payed_user_id), **{"meta_data": meta_data})

            for key, value in email_dict.items() or {}:
                email_payload = {
                    "to_addrs": [key],
                    "subject": SplitBillNotificationTemplate.subject,
                    "body_html": SplitBillNotificationTemplate.body.format(dynamic_body=value)
                }
                await Email.send_email(payload=EmailInBound(**email_payload))

    except Exception as ex:
        logging.error(str(ex))
    finally:
        clear_db_session()


@celery_master_app.task(name="celery_tasks.workers.main.split_amount_task_main")
def split_amount_task_main(id: int):
    """task for split amount"""
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(split_amount_task(_id=id))
    except Exception as ex:
        logging.error(str(ex))
    finally:
        clear_db_session()


async def _split_amount_weekly_task():
    """split amount weekly email task"""
    try:
        user_data = UserModel.get_user()
        for user in user_data:
            pay_body = f""
            take_body = f""
            meta_data = copy.deepcopy(user.meta_data) if user.meta_data else {}
            for key, value in meta_data.items():
                group_data = GroupModel.get_by_id(_id=key)
                for key1, value1 in value.items():
                    pay_body += f"you have to pay"
                    take_body += f"you have to take"
                    for key2, value2 in value1.items():
                        user_data = UserModel.get_user(_id=key2)
                        if key1 == "pay":
                            pay_body += f" {value2}/- to {user_data.name},"
                        if key1 == "take":
                            take_body += f" {value2}/- from {user_data.name},"
                    pay_body += f"for group {group_data.group_name}"
                    take_body += f"for group {group_data.group_name}"
                pay_body += f"<br>"
                take_body += f"<br>"
            body = f" {pay_body} <br><br> {take_body}"
            body = SplitBillNotificationTemplate.body.format(dynamic_body=body)
            email_payload = {
                "to_addrs": [user.email],
                "subject": SplitBillNotificationTemplate.subject,
                "body_html": body
            }
            try:
                await Email.send_email(payload=EmailInBound(**email_payload))
            except Exception as ex:
                logging.error(str(ex))
    except Exception as ex:
        logging.error(str(ex))
    finally:
        clear_db_session()


@celery_master_app.task(name="celery_tasks.workers.main.split_amount_weekly_task")
def split_amount_weekly_task():
    """task for split amount"""
    try:
        if not is_duplicate_task("celery_tasks.workers.main.split_amount_weekly_task"):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(_split_amount_weekly_task())
    except Exception as ex:
        logging.error(str(ex))
    finally:
        clear_db_session()
