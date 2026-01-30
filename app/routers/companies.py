from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyOut

router = APIRouter(prefix="/companies", tags=["companies"])


@router.post("/", response_model=CompanyOut)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company(**company.model_dump())

    db.add(db_company)
    try:
        db.commit()
        db.refresh(db_company)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Company already exists")

    return db_company


@router.get("/", response_model=List[CompanyOut])
def get_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()


@router.get("/{company_id}", response_model=CompanyOut)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.company_id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
