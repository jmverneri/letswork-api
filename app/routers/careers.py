from fastapi import APIRouter, Header, HTTPException
from app.schemas.career import Career
from typing import List

router = APIRouter(prefix="/careers", tags=["Careers"])

# Datos Mock (Igual que los que la API original de la UTN solía devolver)
careers_mock = [
    {"careerId": 1, "description": "Ingeniería Pesquera", "active": True},
    {"careerId": 2, "description": "Ingeniería Naval", "active": True},
    {"careerId": 3, "description": "Técnico Universitario en Procedimientos y Tecnologías Ambientales", "active": True},
    {"careerId": 4, "description": "Técnico Universitario en Producción Textil", "active": True},
    {"careerId": 5, "description": "Técnico Universitario en Administración", "active": True},
    {"careerId": 6, "description": "Técnico Universitario en Programación", "active": True},
    {"careerId": 7, "description": "Técnico Superior en Interiorismo", "active": True}
]

@router.get("/", response_model=List[Career])
async def get_all_careers(x_api_key: str = Header(None)):
    # Verificamos la Key para cumplir con la consigna
    if x_api_key != "4f3bceed-50ba-4461-a910-518598664c08":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    return careers_mock

@router.get("/{career_id}", response_model=Career)
async def get_career_by_id(career_id: int, x_api_key: str = Header(None)):
    if x_api_key != "4f3bceed-50ba-4461-a910-518598664c08":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    career = next((c for c in careers_mock if c["careerId"] == career_id), None)
    if not career:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    return career