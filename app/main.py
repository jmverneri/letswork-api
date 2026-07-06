from fastapi import FastAPI
from app.routers.students import router as students_router
from app.routers.careers import router as careers_router

app = FastAPI(title="UTN Students API Mirror")

app.include_router(students_router)
app.include_router(careers_router)

@app.get("/")
def read_root():
    return {"message": "API de la Universidad funcionando"}