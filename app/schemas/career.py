from pydantic import BaseModel

class CareerCreate(BaseModel):
    name: str


class CareerOut(BaseModel):
    career_id: int
    name: str

    class Config:
        from_attributes = True
