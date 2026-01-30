from pydantic import BaseModel, EmailStr
from typing import Optional

class CompanyCreate(BaseModel):
    name: str
    year_foundation: Optional[int]
    city: Optional[str]
    description: Optional[str]
    logo: Optional[str]
    email: EmailStr
    phone_number: Optional[str]
    cuit: Optional[str]

class CompanyOut(BaseModel):
    company_id: int
    name: str
    year_foundation: Optional[int]
    city: Optional[str]
    description: Optional[str]
    logo: Optional[str]
    email: EmailStr
    phone_number: Optional[str]
    cuit: Optional[str]

    class Config:
        from_attributes = True
