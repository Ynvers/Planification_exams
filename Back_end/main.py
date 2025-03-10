from fastapi import FastAPI, HTTPException
from models import PlanningRequest, PlanningResponse
from planning import planifier_examens

app = FastAPI()

@app.post("/planifier", response_model=PlanningResponse)
def planifier(request: PlanningRequest):
    planning = planifier_examens(
        examens=request.examens,
        salles=request.salles,
        disponibilites=request.disponibilites,
        global_hours=request.global_hours,
        transition=request.transition
    )
    if planning == "Pas de solution trouvée":
        return {"planning": {}, "message": "Aucune solution trouvée pour ce planning"}
    return {"planning": planning, "message": "Solution trouvée"}




# Pour exécuter l'application : uvicorn main:app --reload