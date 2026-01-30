import random
from fastapi import APIRouter, Header, HTTPException
from app.schemas.student import Student
from typing import List
from datetime import date, timedelta

router = APIRouter(prefix="/students", tags=["Students"])

def generate_random_students(count: int):
    first_names = ["Juan", "María", "Lucas", "Ana", "Santiago", "Sofía", "Diego", "Belén", "Nicolás", "Elena"]
    last_names = ["García", "Rodríguez", "López", "Martínez", "González", "Pérez", "Sánchez", "Romero", "Díaz", "Fernández"]
    genders = ["Masculino", "Femenino", "No binario"]
    
    students = []
    for i in range(1, count + 1):
        # Generamos datos aleatorios
        fname = random.choice(first_names)
        lname = random.choice(last_names)
        # El email lo armamos con el nombre y apellido para que sea realista
        email = f"{fname.lower()}.{lname.lower()}{i}@utn.com"
        
        student = {
            "studentId": i,
            "careerId": random.randint(1, 7),  # Asignamos una de las 7 carreras de MDP
            "firstName": fname,
            "lastName": lname,
            "dni": f"{random.randint(30000000, 45000000)}",
            "fileNumber": f"MDP-{1000 + i}",
            "gender": random.choice(genders),
            "birthDate": date(1995, 1, 1) + timedelta(days=random.randint(0, 3650)), # Entre 1995 y 2005
            "email": email,
            "phoneNumber": f"223{random.randint(4000000, 6000000)}",
            "active": True
        }
        students.append(student)
    return students

# Generamos los 50 alumnos al iniciar
students_mock = generate_random_students(50)

# Agregamos a "Juan Verneri" manualmente para que siempre tengas un usuario conocido para testear
students_mock.append({
    "studentId": 51,
    "careerId": 6,
    "firstName": "Juan",
    "lastName": "Verneri",
    "dni": "12345678",
    "fileNumber": "MDP-2000",
    "gender": "Masculino",
    "birthDate": "1998-05-20",
    "email": "juan@utn.com",
    "phoneNumber": "223445566",
    "active": True
})

@router.get("/email/{email}", response_model=Student)
async def get_student_by_email(email: str, x_api_key: str = Header(None)):
    if x_api_key != "4f3bceed-50ba-4461-a910-518598664c08":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    student = next((s for s in students_mock if s["email"].lower() == email.lower()), None)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/", response_model=List[Student])
async def get_all_students(x_api_key: str = Header(None)):
    if x_api_key != "4f3bceed-50ba-4461-a910-518598664c08":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return students_mock