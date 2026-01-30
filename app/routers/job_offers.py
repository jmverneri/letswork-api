from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.job_offer import JobOffer
from app.schemas.job_offer import JobOfferCreate, JobOfferOut

router = APIRouter(prefix="/job-offers", tags=["job-offers"])


@router.post("/", response_model=JobOfferOut)
def create_job_offer(offer: JobOfferCreate, db: Session = Depends(get_db)):
    db_offer = JobOffer(**offer.model_dump())

    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)

    return db_offer


@router.get("/", response_model=List[JobOfferOut])
def list_job_offers(db: Session = Depends(get_db)):
    return db.query(JobOffer).all()


@router.get("/{job_offer_id}", response_model=JobOfferOut)
def get_job_offer(job_offer_id: int, db: Session = Depends(get_db)):
    offer = db.query(JobOffer).filter(JobOffer.job_offer_id == job_offer_id).first()
    if not offer:
        raise HTTPException(status_code=404, detail="Job offer not found")
    return offer
