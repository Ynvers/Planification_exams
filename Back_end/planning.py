from ortools.sat.python import cp_model

def is_available(disponibilites, day, room, hour):
    """Renvoie True si la salle 'room' est disponible à 'hour' le 'day',
       selon les intervalles d'ouverture définis dans disponibilites."""
    if room not in disponibilites.get(day, {}):
        return False
    for interval in disponibilites[day][room]:
        start, end = interval
        # On considère l'heure de début comme disponible, et l'heure 'end' comme non disponible.
        if start <= hour < end:
            return True
    return False

def planifier_examens(examens, salles, disponibilites, global_hours, transition=1):
    model = cp_model.CpModel()
    X = {}
    for e in examens:
        for day in disponibilites:
            for hour in global_hours:
                for room in salles:
                    if is_available(disponibilites, day, room, hour):
                        X[e, day, hour, room] = model.NewBoolVar(f'X_{e}_{day}_{hour}_{room}')
                    else:
                        X[e, day, hour, room] = model.NewConstant(0)

    # Contrainte 1 : Chaque examen doit être programmé exactement une fois.
    for e in examens:
        model.Add(sum(X[e, day, hour, room]
                      for day in disponibilites 
                      for hour in global_hours 
                      for room in salles) == 1)

    # Contrainte 2 : Dans une même salle et au même créneau, plusieurs examens sont autorisés
    # seulement s'ils ont la même durée et proviennent de la même année.
    for day in disponibilites:
        for hour in global_hours:
            for room in salles:
                if is_available(disponibilites, day, room, hour):
                    for e1 in examens:
                        for e2 in examens:
                            if e1 < e2:
                                if (examens[e1].duree != examens[e2].duree) or (examens[e1].annee != examens[e2].annee):
                                    model.Add(X[e1, day, hour, room] + X[e2, day, hour, room] <= 1)

    # Contrainte 3 : Respect de la capacité des salles (en utilisant nb_etudiants)
    for day in disponibilites:
        for hour in global_hours:
            for room in salles:
                if is_available(disponibilites, day, room, hour):
                    model.Add(
                        sum(X[e, day, hour, room] * examens[e].nb_etudiants for e in examens)
                        <= salles[room].capacite  # Utilisation de la notation par point
                    )

    # Contrainte 4 : Les examens de différentes années ne sont pas programmés simultanément,
    # même s'ils sont dans des salles différentes.
    for day in disponibilites:
        for hour in global_hours:
            for e1 in examens:
                for e2 in examens:
                    if e1 < e2 and (examens[e1].annee != examens[e2].annee):
                        model.Add(
                            sum(X[e1, day, hour, room] for room in salles) +
                            sum(X[e2, day, hour, room] for room in salles)
                            <= 1
                        )

    # Contrainte 5 : La disponibilité des salles est respectée (déjà prise en compte lors de la création de X)

    # Contrainte 6 : Transition entre examens dans la même salle.
    for e in examens:
        duree = examens[e].duree
        for day in disponibilites:
            for hour in global_hours:
                for room in salles:
                    if is_available(disponibilites, day, room, hour):
                        for d in range(1, duree + transition):
                            if hour + d in global_hours:
                                model.Add(
                                    X[e, day, hour, room] +
                                    sum(X[e2, day, hour + d, room] for e2 in examens if e2 != e)
                                    <= 1
                                )

    # Objectif : Minimiser le dernier instant d'examen
    dernier_instant = model.NewIntVar(0, max(global_hours), 'dernier_instant')
    for e in examens:
        for day in disponibilites:
            for hour in global_hours:
                for room in salles:
                    if is_available(disponibilites, day, room, hour):
                        model.Add(dernier_instant >= hour).OnlyEnforceIf(X[e, day, hour, room])
    model.Minimize(dernier_instant)

    # Résolution du problème
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        planning = {day: [] for day in disponibilites}
        for e in examens:
            for day in disponibilites:
                for hour in global_hours:
                    for room in salles:
                        if solver.Value(X[e, day, hour, room]) == 1:
                            planning[day].append((hour, e, room, examens[e].annee, examens[e].filiere))
        for day in planning:
            planning[day].sort(key=lambda x: x[0])
        return planning
    else:
        return "Pas de solution trouvée"