from app.database import engine

try:
    with engine.connect() as conn:
        print("✅ Conectado a MySQL")
except Exception as e:
    print("❌ Error de conexión:", e)

