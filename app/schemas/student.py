from pydantic import BaseModel
from typing import Optional
from datetime import date

class StudentBase(BaseModel):
    career_id: Optional[int]
    first_name: str
    last_name: str
    dni: str
    file_number: Optional[str]
    gender: Optional[str]
    birth_date: Optional[date]
    email: str
    phone_number: Optional[str]

class StudentCreate(StudentBase):
    password: str

class StudentOut(StudentBase):
    student_id: int
    active: bool

    class Config:
        from_attributes = True
