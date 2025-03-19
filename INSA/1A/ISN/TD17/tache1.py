import calendrier as cal

LIEN_CALENDRIER = "https://ade-outils.insa-lyon.fr/ADE-Cal:~lpeyronnet!2024-2025:f96ff6e2442808995dadb7c8f88ebea2238501fc"


def tri_evenements(evenements: list):
    """
    Entree :
        - evenements : liste d'evenements
    Sortie :
        Liste 2D d'evenements tries selon le jour et l'heure.
    """
    res = [[] for _ in range(5)]
    # tri par insertion
    for i in range(1, len(evenements)):
        j = i
        while (
            j > 0
            and evenements[j].get("dtstart").dt < evenements[j - 1].get("dtstart").dt
        ):
            evenements[j], evenements[j - 1] = evenements[j - 1], evenements[j]
            j -= 1
    for event in evenements:
        res[event.get("dtstart").dt.weekday()].append(event)
    return res


def obtenir_evenements_semaine(n: int) -> list[list]:
    """
    Obtient les evenements tries de la semaine actuelle + n semaine.
    Exemple : Si n = 1, les evenements de la semaine suivante par rapport a la semaine actuelle seront obtenus.
              Si n = -1, les evenements de la semaine precedente par rapport a la semaine actuelle seront obtenus.
    Retourne : Une liste 2D d'evenements de la semaine [evenements_lundi, evenements_mardi, ...]
    """
    calendrier = cal.creer_calendrier_url(LIEN_CALENDRIER)
    deb = cal.lundi_de_la_semaine(cal.ajouter_jours(cal.aujourdhui(), n * 7))
    fin = cal.ajouter_jours(
        cal.lundi_de_la_semaine(cal.ajouter_jours(cal.aujourdhui(), n * 7)), 5
    )
    events = cal.liste_evenements(calendrier, deb, fin)
    return tri_evenements(events)


def obtenir_evenement_formate(evenement) -> str:
    """
    Obtient le format d'un evenement pour affichage.
    """
    heure_debut = evenement.get("dtstart").dt.strftime("%Hh%M")
    heure_fin = evenement.get("dtend").dt.strftime("%Hh%M")
    # Addition de 1h pour respecter le fuseau horaire de l'utilisateur
    heure_debut = str(int(heure_debut[:2]) + 1) + heure_debut[2:]
    heure_fin = str(int(heure_fin[:2]) + 1) + heure_fin[2:]
    return f"# - de {heure_debut} à {heure_fin} : {extraire_matiere(evenement)}"


def extraire_matiere(evenement) -> str:
    """
    Renvoie le nom de la matiere d'un evenement.
    """
    infos = cal.extraire_description(evenement).split("\n")[1].split("]")
    type_cours = ""
    if ":CM" in infos[0]:
        type_cours = "Amphi"
    elif ":TD" in infos[0]:
        type_cours = "TD"
    elif ":TP" in infos[0]:
        type_cours = "TP"
    elif ":EV" in infos[0]:
        type_cours = "Evaluation"

    return f"{type_cours} {infos[1].strip()}"


def afficher_evenements_semaine(n: int) -> None:
    """
    Affiche les evenements de la semaine actuelle + n.
    """
    events = obtenir_evenements_semaine(n)
    print(f"Semaine {n} :")
    for i in range(len(events)):  # pour chaque jour
        print(
            f"# {cal.ajouter_jours(cal.lundi_de_la_semaine(cal.aujourdhui()), i+7*n).strftime( '%A %d %B')}"
        )
        for event in events[i]:  # pour chaque evenement
            print(obtenir_evenement_formate(event))
        print("##########")


# Programme principal tache 1

programme = True
n = 0

while programme:
    afficher_evenements_semaine(n)
    rep = input(
        "S : semaine suivante, P : semaine precedente, Q : quitter\n-> "
    ).lower()
    if rep == "s":
        n += 1
    elif rep == "p":
        n -= 1
    else:
        programme = False
