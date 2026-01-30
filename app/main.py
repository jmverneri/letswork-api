from fastapi import FastAPI
from app.routers import auth, students, companies, job_offers, careers

app = FastAPI(title="LetsWork API")

app.include_router(auth.router)
app.include_router(students.router)
app.include_router(companies.router)
app.include_router(job_offers.router)
app.include_router(careers.router)

@app.get("/health")
def health():
    return {"status": "ok"}
