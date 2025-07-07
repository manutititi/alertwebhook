from telegram import Bot
from app.config import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

async def send(alert: dict):
    if not settings.TELEGRAM_CHAT_ID:
        print("[telegram] No chat_id configurado.")
        return

    try:
        text = (
            f"🚨 {alert['status'].upper()}: {alert['labels'].get('alertname', 'Unknown')}\n"
            f"🔖 instance: {alert['labels'].get('instance', 'N/A')}\n"
            f"🕒 since: {alert.get('startsAt')}\n"
            f"📄 summary: {alert['annotations'].get('summary', 'No summary')}"
        )
        await bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=text)
        print("[telegram] Mensaje enviado correctamente.")
    except Exception as e:
        print(f"[telegram] Error al enviar mensaje: {e}")
