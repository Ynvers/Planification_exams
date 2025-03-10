from fastapi import FastAPI
from api.endpoints import router as planning_router

app = FastAPI()

# Inclure les routes de l'API
app.include_router(planning_router, prefix="/api")

# Pour exécuter l'application : uvicorn main:app --reload