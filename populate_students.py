# populate_students.py
from sqlalchemy import create_engine, text
from passlib.context import CryptContext
from faker import Faker
import random

# 🔹 Configuración de la DB
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/letswork"
engine = create_engine(DATABASE_URL, echo=True)

# 🔹 Configuración de hash de contraseña
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔹 Generador de datos random
fake = Faker()

# 🔹 Inserción de 10 estudiantes
students = []
for i in range(10):
    first_name = fake.first_name()
    last_name = fake.last_name()
    dni = str(random.randint(20000000, 45000000))
    file_number = f"F{str(i+1).zfill(3)}"
    gender = random.choice(["M", "F"])
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=25).strftime("%Y-%m-%d")
    email = f"{first_name.lower()}.{last_name.lower()}@test.com"
    phone_number = fake.phone_number()
    active = True
    career_id = random.randint(1, 3)
    password = pwd_context.hash("123")  # contraseña "123" para todos
    students.append({
        "career_id": career_id,
        "first_name": first_name,
        "last_name": last_name,
        "dni": dni,
        "file_number": file_number,
        "gender": gender,
        "birth_date": birth_date,
        "email": email,
        "phone_number": phone_number,
        "active": active,
        "password_hash": password
    })

# 🔹 Insertar en DB
with engine.connect() as conn:
    for s in students:
        conn.execute(
            text("""
            INSERT INTO students
            (career_id, first_name, last_name, dni, file_number, gender, birth_date, email, phone_number, active, password_hash)
            VALUES
            (:career_id, :first_name, :last_name, :dni, :file_number, :gender, :birth_date, :email, :phone_number, :active, :password_hash)
            """),
            s
        )
    conn.commit()

print("✅ 10 estudiantes insertados con éxito!")
