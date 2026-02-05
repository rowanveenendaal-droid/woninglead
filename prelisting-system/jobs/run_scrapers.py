from app.database import SessionLocal
from app.models import Lead
from app.airtable import push_lead
from datetime import datetime

db = SessionLocal()

new_leads = [
    {"plaats":"Nijmegen","signaal":"overlijden"},
    {"plaats":"Arnhem","signaal":"scheiding"}
]

for i, dl in enumerate(new_leads, start=1):
    lead = Lead(
        id=i,
        plaats=dl["plaats"],
        signaal=dl["signaal"],
        score=70,
        status="A",
        makelaar_email="info@lokalemakelaar.nl",
        created_at=datetime.now()
    )
    db.add(lead)
    push_lead(lead)

db.commit()
db.close()
print("✅ Scraper + Airtable push klaar")
