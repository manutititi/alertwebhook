import os
import httpx
from app.config import settings

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")

async def send(alert: dict):
    if not DISCORD_WEBHOOK_URL:
        print("[discord] No webhook URL configurada.")
        return

    try:
        title = alert['labels'].get('alertname', 'Unknown Alert')
        instance = alert['labels'].get('instance', 'N/A')
        summary = alert['annotations'].get('summary', 'No summary')
        status = alert.get('status', 'unknown').upper()
        timestamp = alert.get('received_at', '')

        content = f"🚨 **{status}**: {title}\n🔖 `{instance}`\n🕒 `{timestamp}`\n📄 {summary}"

        async with httpx.AsyncClient() as client:
            response = await client.post(DISCORD_WEBHOOK_URL, json={"content": content})

        if response.status_code != 204:
            print(f"[discord] Error al enviar: {response.status_code} {response.text}")
        else:
            print("[discord] Mensaje enviado correctamente.")

    except Exception as e:
        print(f"[discord] Error: {e}")
