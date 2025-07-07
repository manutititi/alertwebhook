from app.platforms import telegram

async def send_alert(alert: dict):
    await telegram.send(alert)
