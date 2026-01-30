from fastapi import FastAPI
from app.routers import student_router, career_router

app = FastAPI(title="UTN Students API Mirror")

# Incluimos las rutas de las carpetas
app.include_router(student_router.router)
# app.include_router(career_router.router)
app.include_router(career_router.router)

@app.get("/")
def read_root():
    return {"message": "API de la Universidad funcionando"}