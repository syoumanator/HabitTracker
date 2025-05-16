import requests
from config import settings


def message_telegram(message, chat_id):
    """Telegram сообщение"""
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    response = requests.get(f"{settings.TG_URL}{settings.TG_TOKEN}/sendMessage",params=params,timeout=10,)
    if not response.ok:
        raise RuntimeError("Отказ отправки сообщения")
