from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True)
    plaats = Column(String)
    signaal = Column(String)
    score = Column(Float)
    status = Column(String, default="nieuw")
    makelaar_email = Column(String)
    created_at = Column(Date, default=datetime.now)
    laatst_benaderd = Column(Date)
    opmerkingen = Column(String)
