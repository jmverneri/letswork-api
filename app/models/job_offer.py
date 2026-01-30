from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from app.database import Base

class JobOffer(Base):
    __tablename__ = "job_offers"

    job_offer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    start_day = Column(Date)
    deadline = Column(Date)
    salary = Column(Integer)
    active = Column(Boolean, default=True)

    company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)
    career_id = Column(Integer, ForeignKey("careers.career_id"), nullable=True)
    job_position_id = Column(Integer, ForeignKey("job_positions.job_position_id"), nullable=True)
