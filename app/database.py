from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/letswork"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependency para FastAPI: cada endpoint que necesite DB llama a esto
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
