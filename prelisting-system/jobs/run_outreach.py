from app.database import SessionLocal
from app.models import Lead
from app.mailer import send_mail

db = SessionLocal()
leads = db.query(Lead).filter(Lead.status=="A").all()

for lead in leads:
    send_mail(lead.makelaar_email, f"Pre-listing kans in {lead.plaats}", f"Status: {lead.status}", test_mode=True)
    lead.status = "Benaderd"

db.commit()
db.close()
print("✅ Outreach run klaar")
