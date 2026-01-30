from pydantic import BaseModel
from datetime import date

class Student(BaseModel):
    studentId: int
    careerId: int
    firstName: str
    lastName: str
    dni: str
    fileNumber: str
    gender: str
    birthDate: date
    email: str
    phoneNumber: str
    active: bool

    class Config:
        from_attributes = True