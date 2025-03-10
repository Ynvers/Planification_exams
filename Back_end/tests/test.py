import requests

url = "http://127.0.0.1:8000/planifier"
headers = {"Content-Type": "application/json"}
data = {
    "examens": {
        "Maths": {"duree": 2, "annee": 2024, "filiere": "Informatique", "nb_etudiants": 30},
        "Physique": {"duree": 1, "annee": 2024, "filiere": "Electronique", "nb_etudiants": 25}
    },
    "salles": {
        "Salle_101": {"capacite": 40},
        "Salle_102": {"capacite": 30}
    },
    "disponibilites": {
        "Salle_101": {"2024-06-30": [[8, 12], [14, 18]]},
        "Salle_102": {"2024-06-30": [[9, 13], [15, 17]]}
    },
    "global_hours": [8, 18],
    "transition": 1
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code, response.json())
