from fastapi import APIRouter, HTTPException
from models import PlanningRequest, PlanningResponse
from services.planning import planifier_examens

router = APIRouter()

@router.post("/planifier", response_model=PlanningResponse)
def planifier(request: PlanningRequest):
    planning = planifier_examens(
        examens=request.examens,
        salles=request.salles,
        disponibilites=request.disponibilites,
        global_hours=request.global_hours,
        transition=request.transition
    )
    if planning == "Pas de solution trouvée":
        raise HTTPException(status_code=400, detail="Pas de solution trouvée")
    return {"planning": planning}

