from sqlalchemy import Column, Integer, String
from app.database import Base

class Career(Base):
    __tablename__ = "careers"

    career_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
