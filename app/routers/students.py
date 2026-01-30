from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentOut
from passlib.context import CryptContext

router = APIRouter(prefix="/students", tags=["students"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return db.query(Student).get(student_id)

@router.post("/", response_model=StudentOut)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(
        **student.model_dump(exclude={"password"}),
        password_hash=pwd_context.hash(student.password)
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
