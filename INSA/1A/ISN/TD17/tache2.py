import calendrier as cal

LIEN_CALENDRIER = "https://insa-utils.fr/cal/get.php?url=https://ade-outils.insa-lyon.fr/ADE-Cal:~lpeyronnet!2024-2025:f96ff6e2442808995dadb7c8f88ebea2238501fc&desc=true&count=true&types=general_sport,lang,sport,huma,support,p2i,other,*&ctypes=*,group,td,cm,tp,ev,soutien"


def tri_evenements(evenements: list):
    """
  Entree : 
      - evenements : liste d'evenements
  Sortie :
      Liste 2D d'evenements tries selon le jour et l'heure.
  """
    res = []
    # tri par insertion
    for i in range(1, len(evenements)):
        j = i
        while j > 0 and evenements[j].get('dtstart').dt < evenements[
                j - 1].get("dtstart").dt:
            evenements[j], evenements[j - 1] = evenements[j - 1], evenements[j]
            j -= 1

    for i in range(len(evenements)):
        # Vérifier si event commence par EV
        if evenements[
                i] is not None and "EV" in f"{evenements[i].get('summary')}":
            res.append(evenements[i])

    return res


def nombre_semaine_restantes() -> int:
    """
    Retourne le nombre de semaines restantes avant la fin du semestre.
    """
    date_fin_semestre = cal.creer_date(2025, 9, 1)
    date_aujourdhui = cal.aujourdhui()
    return (date_fin_semestre.replace(tzinfo=None) -
            date_aujourdhui.replace(tzinfo=None)).days // 7


def recuperer_evenements(n: int) -> list[list]:
    """
      Obtient les evenements tries de la semaine actuelle + n semaine.
      Exemple : Si n = 1, les evenements de la semaine suivante par rapport a la semaine actuelle seront obtenus.
                Si n = -1, les evenements de la semaine precedente par rapport a la semaine actuelle seront obtenus.
      Retourne : Une liste 2D d'evenements de la semaine [evenements_lundi, evenements_mardi, ...]
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
    date = evenement.get('dtstart').dt
    heure_debut = date.strftime('%Hh%M')
    heure_fin = evenement.get('dtend').dt.strftime('%Hh%M')
    # Addition de 2h pour respecter le fuseau horaire de l'utilisateur
    heure_debut = str(int(heure_debut[:2]) + 2) + heure_debut[2:]
    heure_fin = str(int(heure_fin[:2]) + 2) + heure_fin[2:]
    return f"{date.strftime('%A %d %B %Y')} de {heure_debut} à {heure_fin} : {evenement.get('summary')}".replace(
        "EV", "IE")


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
