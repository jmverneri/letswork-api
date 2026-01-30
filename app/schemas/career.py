from pydantic import BaseModel

class Career(BaseModel):
    careerId: int
    description: str
    active: bool

    class Config:
        from_attributes = True