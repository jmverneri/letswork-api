from pydantic import BaseModel
from typing import Optional
from datetime import date

class JobOfferCreate(BaseModel):
    name: str
    description: Optional[str]
    start_day: Optional[date]
    deadline: Optional[date]
    salary: Optional[int]
    company_id: int
    career_id: Optional[int]
    job_position_id: Optional[int]


class JobOfferOut(BaseModel):
    job_offer_id: int
    name: str
    description: Optional[str]
    start_day: Optional[date]
    deadline: Optional[date]
    salary: Optional[int]
    active: bool
    company_id: int
    career_id: Optional[int]
    job_position_id: Optional[int]

    class Config:
        from_attributes = True  # reemplaza orm_mode
