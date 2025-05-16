from celery import shared_task
from django.conf import settings
from datetime import datetime, timedelta
from habit.models import Habits
import pytz
from habit.services import message_telegram


@shared_task
def telegram_notice():
    zone = pytz.timezone(settings.TIME_ZONE)
    habits = Habits.objects.filter(
        time__lte=(datetime.now(zone)).time(),
        time__gte=(datetime.now(zone) - timedelta(minutes=5)).time()
    )
    for habit in habits:
        user_tg = habit.user.tg_chat_id
        if user_tg:
            message = f"Я буду {habit.action} в {habit.time} в {habit.place}"
            message_telegram()
