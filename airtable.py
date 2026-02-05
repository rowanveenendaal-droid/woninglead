import requests
from app.config import *

AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE}"
HEADERS = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json"
}

def push_lead(lead):
    data = {
        "fields": {
            "lead_id": str(lead.id),
            "plaats": lead.plaats,
            "signaal": lead.signaal,
            "score": lead.score,
            "status": lead.status,
            "makelaar_email": lead.makelaar_email,
            "created_at": lead.created_at.isoformat()
        }
    }
    r = requests.post(AIRTABLE_URL, json=data, headers=HEADERS)
    if r.status_code not in (200, 201):
        print("⚠️ Error pushing lead:", r.text)
    else:
        print(f"✅ Lead {lead.id} gepusht naar Airtable")
