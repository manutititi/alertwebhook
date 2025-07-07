import os
from typing import Callable, Awaitable
from app.config import settings

# Mapa de plataformas a funciones (solo se cargan si están configuradas)
PLATFORM_SENDERS: dict[str, Callable[[dict], Awaitable[None]]] = {}

# --- Telegram ---
if settings.TELEGRAM_BOT_TOKEN and settings.TELEGRAM_CHAT_ID:
    from app.platforms import telegram
    PLATFORM_SENDERS["telegram"] = telegram.send

# --- Discord ---
if os.getenv("DISCORD_WEBHOOK_URL"):
    from app.platforms import discord
    PLATFORM_SENDERS["discord"] = discord.send


# if os.getenv("SLACK_WEBHOOK_URL"):
#     from app.platforms import slack
#     PLATFORM_SENDERS["slack"] = slack.send


async def send_alert(alert: dict):
    if not PLATFORM_SENDERS:
        print("[dispatcher] No hay plataformas configuradas para enviar alertas.")
        return

    for name, sender in PLATFORM_SENDERS.items():
        try:
            await sender(alert)
        except Exception as e:
            print(f"[dispatcher] Error enviando alerta a {name}: {e}")
