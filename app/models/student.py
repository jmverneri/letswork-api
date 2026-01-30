from sqlalchemy import Column, Integer, String, Boolean, Date
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    career_id = Column(Integer, nullable=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    dni = Column(String(20), unique=True)
    file_number = Column(String(50), nullable=True)
    gender = Column(String(20), nullable=True)
    birth_date = Column(Date, nullable=True)
    email = Column(String(255), unique=True, index=True)
    phone_number = Column(String(50), nullable=True)
    active = Column(Boolean, default=True)
    password_hash = Column(String(255))

