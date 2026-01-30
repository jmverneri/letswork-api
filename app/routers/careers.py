from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.career import Career
from app.schemas.career import CareerCreate, CareerOut

router = APIRouter(prefix="/careers", tags=["careers"])


@router.post("/", response_model=CareerOut)
def create_career(career: CareerCreate, db: Session = Depends(get_db)):
    existing = db.query(Career).filter(Career.name == career.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Career already exists")

    db_career = Career(**career.model_dump())
    db.add(db_career)
    db.commit()
    db.refresh(db_career)

    return db_career


@router.get("/", response_model=List[CareerOut])
def list_careers(db: Session = Depends(get_db)):
    return db.query(Career).all()


@router.get("/{career_id}", response_model=CareerOut)
def get_career(career_id: int, db: Session = Depends(get_db)):
    career = db.query(Career).filter(Career.career_id == career_id).first()
    if not career:
        raise HTTPException(status_code=404, detail="Career not found")
    return career
