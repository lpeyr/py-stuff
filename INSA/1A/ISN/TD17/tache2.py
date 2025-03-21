import calendrier as cal

LIEN_CALENDRIER = "https://ade-outils.insa-lyon.fr/ADE-Cal:~lpeyronnet!2024-2025:f96ff6e2442808995dadb7c8f88ebea2238501fc"


def tri_evenements(evenements: list):
    """
    Entree :
        - evenements : liste d'evenements
    Sortie :
        Liste d'evenements tries selon le jour et l'heure.
    """
    res = []
    # tri par insertion
    for i in range(1, len(evenements)):
        j = i
        while (
            j > 0
            and evenements[j].get("dtstart").dt < evenements[j - 1].get("dtstart").dt
        ):
            evenements[j], evenements[j - 1] = evenements[j - 1], evenements[j]
            j -= 1

    for i in range(len(evenements)):
        # Vérifier si event commence par EV
        if evenements[i] is not None and "EV" in f"{evenements[i].get('summary')}":
            res.append(evenements[i])

    return res


def nombre_semaine_restantes() -> int:
    """
    Retourne le nombre de semaines restantes avant la fin du semestre.
    """
    date_fin_semestre = cal.creer_date(2025, 9, 1)
    date_aujourdhui = cal.aujourdhui()
    return (
        date_fin_semestre.replace(tzinfo=None) - date_aujourdhui.replace(tzinfo=None)
    ).days // 7


def recuperer_evenements(n: int) -> list:
    """
    Obtient les evenements tries de la semaine actuelle jusqu'a n semaines plus tard.
    Retourne : Une liste d'evenements
    """
    calendrier = cal.creer_calendrier_url(LIEN_CALENDRIER)
    deb = cal.lundi_de_la_semaine(cal.aujourdhui())
    fin = cal.ajouter_jours(cal.lundi_de_la_semaine(cal.aujourdhui()), n * 7)
    events = cal.liste_evenements(calendrier, deb, fin)
    return tri_evenements(events)


def obtenir_evenement_formate(evenement) -> str:
    """
    Obtient le format d'un evenement pour affichage.
    """
    date = evenement.get("dtstart").dt
    heure_debut = date.strftime("%Hh%M")
    heure_fin = evenement.get("dtend").dt.strftime("%Hh%M")

    # Addition de 2h pour respecter le fuseau horaire de l'utilisateur
    heure_debut = str(int(heure_debut[:2]) + 2) + heure_debut[2:]
    heure_fin = str(int(heure_fin[:2]) + 2) + heure_fin[2:]
    return f"{date.strftime('%A %d %B %Y')} de {heure_debut} à {heure_fin} : {extraire_matiere(evenement)}"


def extraire_matiere(evenement) -> str:
    """
    Renvoie le nom de la matiere d'un evenement.
    """
    infos = (
        cal.extraire_description(evenement).split("\n")[1].split("]")
    )  # Obtient le nom de la matière
    title = cal.extraire_titre(evenement)
    return f"IE{title[-1]} - {infos[1].strip()}"  # Le dernier caractère correspond au numéro de l'IE


def afficher(events):
    """
    Affiche les evenements de la liste d'evenements formates.
    """
    print("#### Prochaines évaluations ####")
    for event in events:
        print(obtenir_evenement_formate(event))


# Programme principal tache 2
evenements = recuperer_evenements(nombre_semaine_restantes())
afficher(evenements)
