from fastapi import FastAPI, Request
from datetime import datetime
from zoneinfo import ZoneInfo
from app.config import settings
from app.logger import logger
from app.models import WebhookPayload
from app.dispatcher import send_alert
import json

app = FastAPI()

def now_tz():
    return datetime.now(ZoneInfo(settings.TIMEZONE)).isoformat()

@app.post("/alert")
async def alert(payload: WebhookPayload, request: Request):
    timestamp = now_tz()
    for alert in payload.alerts:
        alert_dict = alert.dict()
        alert_dict["received_at"] = timestamp
        logger.info(json.dumps(alert_dict))
        await send_alert(alert_dict)  # <-- CAMBIO AQUÍ

    return {"status": "ok", "alerts_received": len(payload.alerts)}
