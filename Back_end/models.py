from pydantic import BaseModel
from typing import Dict, List, Tuple

class Exam(BaseModel):
    duree: int
    annee: int
    filiere: str
    nb_etudiants: int

class Room(BaseModel):
    capacite: int

class Disponibilite(BaseModel):
    intervals: List[Tuple[int, int]]

class PlanningRequest(BaseModel):
    examens: Dict[str, Exam]
    salles: Dict[str, Room]
    disponibilites: Dict[str, Dict[str, List[Tuple[int, int]]]]
    global_hours: List[int]
    transition: int = 1

class PlanningResponse(BaseModel):
    planning: Dict[str, List[Tuple[int, str, str, int, str]]]
    message: str = "Solution trouvée"