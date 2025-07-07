from pydantic import BaseModel
from typing import List, Dict

class Alert(BaseModel):
    status: str
    labels: Dict[str, str]
    annotations: Dict[str, str]
    startsAt: str
    endsAt: str
    generatorURL: str

class WebhookPayload(BaseModel):
    alerts: List[Alert]
