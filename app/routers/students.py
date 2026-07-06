import random
from fastapi import APIRouter, Header, HTTPException
from app.schemas.student import Student
from typing import List
from datetime import date, timedelta
from app.config import API_KEY_REQUIRED

router = APIRouter(prefix="/students", tags=["Students"])

students_mock = [
    {"studentId": 1, "careerId": 6, "firstName": "Juan", "lastName": "Verneri", "dni": "12345678", "fileNumber": "MDP-1001", "gender": "Masculino", "birthDate": "1998-05-20", "email": "juan@utn.com", "phoneNumber": "223445566", "active": True},
    {"studentId": 2, "careerId": 1, "firstName": "Lucas", "lastName": "Gomez", "dni": "35123456", "fileNumber": "MDP-1002", "gender": "Masculino", "birthDate": "1996-03-15", "email": "lucas.gomez2@utn.com", "phoneNumber": "223556677", "active": True},
    {"studentId": 3, "careerId": 2, "firstName": "Maria", "lastName": "Rodriguez", "dni": "38444555", "fileNumber": "MDP-1003", "gender": "Femenino", "birthDate": "1999-11-02", "email": "maria.rodriguez3@utn.com", "phoneNumber": "223112233", "active": True},
    {"studentId": 4, "careerId": 6, "firstName": "Santiago", "lastName": "Lopez", "dni": "40111222", "fileNumber": "MDP-1004", "gender": "Masculino", "birthDate": "2001-07-22", "email": "santiago.lopez4@utn.com", "phoneNumber": "223998877", "active": True},
    {"studentId": 5, "careerId": 5, "firstName": "Ana", "lastName": "Martinez", "dni": "37222333", "fileNumber": "MDP-1005", "gender": "Femenino", "birthDate": "1997-01-30", "email": "ana.martinez5@utn.com", "phoneNumber": "223665544", "active": True},
    {"studentId": 6, "careerId": 3, "firstName": "Diego", "lastName": "Gonzalez", "dni": "42333444", "fileNumber": "MDP-1006", "gender": "Masculino", "birthDate": "2003-05-12", "email": "diego.gonzalez6@utn.com", "phoneNumber": "223334455", "active": True},
    {"studentId": 7, "careerId": 7, "firstName": "Belen", "lastName": "Perez", "dni": "39555666", "fileNumber": "MDP-1007", "gender": "Femenino", "birthDate": "2000-09-18", "email": "belen.perez7@utn.com", "phoneNumber": "223009988", "active": True},
    {"studentId": 8, "careerId": 4, "firstName": "Nicolas", "lastName": "Sanchez", "dni": "41666777", "fileNumber": "MDP-1008", "gender": "Masculino", "birthDate": "2002-02-25", "email": "nicolas.sanchez8@utn.com", "phoneNumber": "223441122", "active": True},
    {"studentId": 9, "careerId": 1, "firstName": "Elena", "lastName": "Diaz", "dni": "36777888", "fileNumber": "MDP-1009", "gender": "Femenino", "birthDate": "1995-12-10", "email": "elena.diaz9@utn.com", "phoneNumber": "223778899", "active": True},
    {"studentId": 10, "careerId": 6, "firstName": "Facundo", "lastName": "Fernandez", "dni": "43888999", "fileNumber": "MDP-1010", "gender": "Masculino", "birthDate": "2004-04-05", "email": "facundo.fernandez10@utn.com", "phoneNumber": "223112244", "active": True},
    {"studentId": 11, "careerId": 2, "firstName": "Sofia", "lastName": "Alvarez", "dni": "34999000", "fileNumber": "MDP-1011", "gender": "Femenino", "birthDate": "1994-08-14", "email": "sofia.alvarez11@utn.com", "phoneNumber": "223554433", "active": True},
    {"studentId": 12, "careerId": 3, "firstName": "Mateo", "lastName": "Torres", "dni": "40123987", "fileNumber": "MDP-1012", "gender": "Masculino", "birthDate": "2001-03-21", "email": "mateo.torres12@utn.com", "phoneNumber": "223667788", "active": True},
    {"studentId": 13, "careerId": 4, "firstName": "Valentina", "lastName": "Ruiz", "dni": "38234765", "fileNumber": "MDP-1013", "gender": "Femenino", "birthDate": "1999-06-30", "email": "valentina.ruiz13@utn.com", "phoneNumber": "223223344", "active": True},
    {"studentId": 14, "careerId": 5, "firstName": "Joaquin", "lastName": "Vazquez", "dni": "42098123", "fileNumber": "MDP-1014", "gender": "Masculino", "birthDate": "2003-11-15", "email": "joaquin.vazquez14@utn.com", "phoneNumber": "223445511", "active": True},
    {"studentId": 15, "careerId": 7, "firstName": "Camila", "lastName": "Castro", "dni": "36111222", "fileNumber": "MDP-1015", "gender": "Femenino", "birthDate": "1995-02-05", "email": "camila.castro15@utn.com", "phoneNumber": "223889900", "active": True},
    {"studentId": 16, "careerId": 6, "firstName": "Agustin", "lastName": "Suarez", "dni": "39456789", "fileNumber": "MDP-1016", "gender": "Masculino", "birthDate": "2000-12-28", "email": "agustin.suarez16@utn.com", "phoneNumber": "223111222", "active": True},
    {"studentId": 17, "careerId": 1, "firstName": "Martina", "lastName": "Blanco", "dni": "41321654", "fileNumber": "MDP-1017", "gender": "Femenino", "birthDate": "2002-04-12", "email": "martina.blanco17@utn.com", "phoneNumber": "223444555", "active": True},
    {"studentId": 18, "careerId": 2, "firstName": "Tomas", "lastName": "Molina", "dni": "37543210", "fileNumber": "MDP-1018", "gender": "Masculino", "birthDate": "1997-09-09", "email": "tomas.molina18@utn.com", "phoneNumber": "223777888", "active": True},
    {"studentId": 19, "careerId": 3, "firstName": "Victoria", "lastName": "Morales", "dni": "35876543", "fileNumber": "MDP-1019", "gender": "Femenino", "birthDate": "1996-01-25", "email": "victoria.morales19@utn.com", "phoneNumber": "223000111", "active": True},
    {"studentId": 20, "careerId": 4, "firstName": "Bruno", "lastName": "Ortega", "dni": "43987654", "fileNumber": "MDP-1020", "gender": "Masculino", "birthDate": "2004-10-31", "email": "bruno.ortega20@utn.com", "phoneNumber": "223222333", "active": True},
    {"studentId": 21, "careerId": 6, "firstName": "Julieta", "lastName": "Delgado", "dni": "38123444", "fileNumber": "MDP-1021", "gender": "Femenino", "birthDate": "1999-05-15", "email": "julieta.delgado21@utn.com", "phoneNumber": "223333444", "active": True},
    {"studentId": 22, "careerId": 1, "firstName": "Ignacio", "lastName": "Ortiz", "dni": "40111000", "fileNumber": "MDP-1022", "gender": "Masculino", "birthDate": "2001-08-20", "email": "ignacio.ortiz22@utn.com", "phoneNumber": "223444333", "active": True},
    {"studentId": 23, "careerId": 2, "firstName": "Delfina", "lastName": "Marin", "dni": "37000999", "fileNumber": "MDP-1023", "gender": "Femenino", "birthDate": "1997-02-14", "email": "delfina.marin23@utn.com", "phoneNumber": "223555666", "active": True},
    {"studentId": 24, "careerId": 3, "firstName": "Ramiro", "lastName": "Soto", "dni": "42555666", "fileNumber": "MDP-1024", "gender": "Masculino", "birthDate": "2003-03-10", "email": "ramiro.soto24@utn.com", "phoneNumber": "223666777", "active": True},
    {"studentId": 25, "careerId": 5, "firstName": "Lola", "lastName": "Luna", "dni": "39444333", "fileNumber": "MDP-1025", "gender": "Femenino", "birthDate": "2000-11-25", "email": "lola.luna25@utn.com", "phoneNumber": "223777000", "active": True},
    {"studentId": 26, "careerId": 7, "firstName": "Enzo", "lastName": "Silva", "dni": "41222111", "fileNumber": "MDP-1026", "gender": "Masculino", "birthDate": "2002-06-05", "email": "enzo.silva26@utn.com", "phoneNumber": "223888111", "active": True},
    {"studentId": 27, "careerId": 6, "firstName": "Abril", "lastName": "Rojas", "dni": "36123321", "fileNumber": "MDP-1027", "gender": "Femenino", "birthDate": "1995-09-17", "email": "abril.rojas27@utn.com", "phoneNumber": "223111000", "active": True},
    {"studentId": 28, "careerId": 1, "firstName": "Bautista", "lastName": "Acosta", "dni": "43000111", "fileNumber": "MDP-1028", "gender": "Masculino", "birthDate": "2004-01-22", "email": "bautista.acosta28@utn.com", "phoneNumber": "223999888", "active": True},
    {"studentId": 29, "careerId": 2, "firstName": "Malena", "lastName": "Medina", "dni": "35888999", "fileNumber": "MDP-1029", "gender": "Femenino", "birthDate": "1996-07-07", "email": "malena.medina29@utn.com", "phoneNumber": "223666555", "active": True},
    {"studentId": 30, "careerId": 4, "firstName": "Felipe", "lastName": "Herrera", "dni": "40777666", "fileNumber": "MDP-1030", "gender": "Masculino", "birthDate": "2001-12-12", "email": "felipe.herrera30@utn.com", "phoneNumber": "223444111", "active": True},
    {"studentId": 31, "careerId": 6, "firstName": "Mia", "lastName": "Aguirre", "dni": "38111999", "fileNumber": "MDP-1031", "gender": "Femenino", "birthDate": "1999-04-04", "email": "mia.aguirre31@utn.com", "phoneNumber": "223222888", "active": True},
    {"studentId": 32, "careerId": 1, "firstName": "Simon", "lastName": "Cano", "dni": "42666555", "fileNumber": "MDP-1032", "gender": "Masculino", "birthDate": "2003-09-09", "email": "simon.cano32@utn.com", "phoneNumber": "223111777", "active": True},
    {"studentId": 33, "careerId": 3, "firstName": "Juana", "lastName": "Guzman", "dni": "36444111", "fileNumber": "MDP-1033", "gender": "Femenino", "birthDate": "1995-03-03", "email": "juana.guzman33@utn.com", "phoneNumber": "223555222", "active": True},
    {"studentId": 34, "careerId": 5, "firstName": "Gael", "lastName": "Romero", "dni": "41999222", "fileNumber": "MDP-1034", "gender": "Masculino", "birthDate": "2002-10-10", "email": "gael.romero34@utn.com", "phoneNumber": "223777333", "active": True},
    {"studentId": 35, "careerId": 7, "firstName": "Clara", "lastName": "Sosa", "dni": "39111888", "fileNumber": "MDP-1035", "gender": "Femenino", "birthDate": "2000-01-01", "email": "clara.sosa35@utn.com", "phoneNumber": "223888444", "active": True},
    {"studentId": 36, "careerId": 6, "firstName": "Benicio", "lastName": "Duarte", "dni": "43222777", "fileNumber": "MDP-1036", "gender": "Masculino", "birthDate": "2004-06-06", "email": "benicio.duarte36@utn.com", "phoneNumber": "223999555", "active": True},
    {"studentId": 37, "careerId": 2, "firstName": "Zoe", "lastName": "Mendez", "dni": "35333666", "fileNumber": "MDP-1037", "gender": "Femenino", "birthDate": "1996-08-08", "email": "zoe.mendez37@utn.com", "phoneNumber": "223666000", "active": True},
    {"studentId": 38, "careerId": 4, "firstName": "Leonel", "lastName": "Paz", "dni": "40444999", "fileNumber": "MDP-1038", "gender": "Masculino", "birthDate": "2001-11-11", "email": "leonel.paz38@utn.com", "phoneNumber": "223444777", "active": True},
    {"studentId": 39, "careerId": 1, "firstName": "Lara", "lastName": "Vega", "dni": "37555000", "fileNumber": "MDP-1039", "gender": "Femenino", "birthDate": "1997-02-02", "email": "lara.vega39@utn.com", "phoneNumber": "223333111", "active": True},
    {"studentId": 40, "careerId": 3, "firstName": "Elias", "lastName": "Rios", "dni": "42111444", "fileNumber": "MDP-1040", "gender": "Masculino", "birthDate": "2003-05-05", "email": "elias.rios40@utn.com", "phoneNumber": "223111999", "active": True},
    {"studentId": 41, "careerId": 5, "firstName": "Emma", "lastName": "Miranda", "dni": "38666222", "fileNumber": "MDP-1041", "gender": "Femenino", "birthDate": "1999-07-07", "email": "emma.miranda41@utn.com", "phoneNumber": "223555000", "active": True},
    {"studentId": 42, "careerId": 7, "firstName": "Ivan", "lastName": "Cordoba", "dni": "40999333", "fileNumber": "MDP-1042", "gender": "Masculino", "birthDate": "2001-09-09", "email": "ivan.cordoba42@utn.com", "phoneNumber": "223777444", "active": True},
    {"studentId": 43, "careerId": 6, "firstName": "Alma", "lastName": "Navarro", "dni": "36222888", "fileNumber": "MDP-1043", "gender": "Femenino", "birthDate": "1995-12-12", "email": "alma.navarro43@utn.com", "phoneNumber": "223888666", "active": True},
    {"studentId": 44, "careerId": 2, "firstName": "Franco", "lastName": "Correa", "dni": "43777111", "fileNumber": "MDP-1044", "gender": "Masculino", "birthDate": "2004-03-03", "email": "franco.correa44@utn.com", "phoneNumber": "223999111", "active": True},
    {"studentId": 45, "careerId": 4, "firstName": "Julia", "lastName": "Orellana", "dni": "35111444", "fileNumber": "MDP-1045", "gender": "Femenino", "birthDate": "1996-06-06", "email": "julia.orellana45@utn.com", "phoneNumber": "223666222", "active": True},
    {"studentId": 46, "careerId": 1, "firstName": "Noah", "lastName": "Paredes", "dni": "41555222", "fileNumber": "MDP-1046", "gender": "Masculino", "birthDate": "2002-08-08", "email": "noah.paredes46@utn.com", "phoneNumber": "223444000", "active": True},
    {"studentId": 47, "careerId": 3, "firstName": "Sara", "lastName": "Gimenez", "dni": "37000333", "fileNumber": "MDP-1047", "gender": "Femenino", "birthDate": "1997-10-10", "email": "sara.gimenez47@utn.com", "phoneNumber": "223222555", "active": True},
    {"studentId": 48, "careerId": 5, "firstName": "Uriel", "lastName": "Farías", "dni": "42888666", "fileNumber": "MDP-1048", "gender": "Masculino", "birthDate": "2003-12-12", "email": "uriel.farias48@utn.com", "phoneNumber": "223111444", "active": True},
    {"studentId": 49, "careerId": 7, "firstName": "Paz", "lastName": "Vidal", "dni": "39444777", "fileNumber": "MDP-1049", "gender": "Femenino", "birthDate": "2000-05-05", "email": "paz.vidal49@utn.com", "phoneNumber": "223000999", "active": True},
    {"studentId": 50, "careerId": 6, "firstName": "Marcos", "lastName": "Benitez", "dni": "34111222", "fileNumber": "MDP-1050", "gender": "Masculino", "birthDate": "1994-01-01", "email": "marcos.benitez50@utn.com", "phoneNumber": "223555888", "active": True}
]

@router.get("/email/{email}", response_model=Student)
async def get_student_by_email(email: str, x_api_key: str = Header(None)):
    if x_api_key != API_KEY_REQUIRED:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    student = next((s for s in students_mock if s["email"].lower() == email.lower()), None)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")    
    return student

@router.get("/", response_model=List[Student])
async def get_all_students(x_api_key: str = Header(None)):
    if x_api_key != API_KEY_REQUIRED:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return students_mock