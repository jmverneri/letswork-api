from sqlalchemy import Column, Integer, String
from app.database import Base

class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    year_foundation = Column(Integer, nullable=True)
    city = Column(String(100), nullable=True)
    description = Column(String(255), nullable=True)
    logo = Column(String(255), nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(50), nullable=True)
    cuit = Column(String(20), unique=True, nullable=True)
