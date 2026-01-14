import json
import matplotlib.pyplot as plt


def plot_graphe(dico, block=True):
    fig, ax = plt.subplots()
    min_x = 500
    max_x = 0
    min_y = 500
    max_y = 0
    for n in dico.values():
        x = n["geometry"]["coordinates"][0]
        y = n["geometry"]["coordinates"][1]
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

        point = plt.Circle((x, y), 0.0001, color="red")
        ax.add_patch(point)
        for v in n["voisins"]:
            xv = dico[v]["geometry"]["coordinates"][0]
            yv = dico[v]["geometry"]["coordinates"][1]
            arc = plt.Line2D([x, xv], [y, yv], color="blue")
            ax.add_line(arc)
    ax.set_xlim(min_x - 0.001, max_x + 0.001)
    ax.set_ylim(min_y - 0.001, max_y + 0.001)
    plt.show(block=block)


def ouvrir_json(file):
    """Fonction qui ouvre un fichier .json dont le nom est passé en paramètre"""
    with open(file, "r") as f:
        d = json.load(f)
        return d["features"]


def dictionnaire_liens(file):
    """
    file: fichier json contenant les liens d'un quartier de la métropole
    renvoie un dictionnaire des liens dont les clés sont les codes de troncon et les valeurs sont un dictionnaire contenant le nom, la commune et le type de circulation du lien
    """
    liste_liens = ouvrir_json(file)
    dico_liens = {}
    for lien in liste_liens:
        code = lien["properties"]["codetroncon"]
        dico_liens[code] = {
            "nom": lien["properties"]["nom"],
            "commune": lien["properties"]["nomcommune"],
            "typecirculation": lien["properties"]["typecirculation"],
        }

    return dico_liens


def dictionnaire_noeuds(file):
    """
    file: fichier json contenant les noeuds de la métropole
    renvoie un dictionnaire des noeuds dont les clés sont les identifiants et les valeurs sont un dictionnaire contenant le nom du noeud (nom), la liste des identifiants des liens auxquels il est relié (incidence) et ses coordonnées GPS (geometry, ce nom de clé est nécessaire pour respecter le format geojson)
    """
    liste_noeuds = ouvrir_json(file)
    dico_noeuds = {}
    for noeud in liste_noeuds:
        id = noeud["properties"]["identifiant"]
        inter = noeud["properties"].get("identtroncon")
        if inter is not None:  # On droppe les noeuds sans lien => erreur de fichier
            incidence = list(
                set(inter.split("|"))
            )  # construction de l'ensemble des liens indicent au noeud, sans doublon
            dico_noeuds[id] = {
                "incidence": incidence,
                "nom": noeud["properties"]["libellecarrefour"],
                "geometry": noeud["geometry"],
            }
    print(len(liste_noeuds), len(dico_noeuds))
    return dico_noeuds


def selectionner_liens_graphe(dico_noeuds, dico_liens):
    """
    dico_noeuds: dictionnaire contenant les noeuds de la métropole
    dico_liens: dictionnaire contenant les liens d'un quartier de la métropole
    renvoie le dictionnaire des copies des liens de dico_liens
        - qui ont 2 extrémités dans dico_noeuds
        - auxquels on rajoute la clé extremites dans laquelle on liste les identifiants des noeuds aux extrémités
    """
    dico_liens_graphe = dict()

    for id, noeud in dico_noeuds.items():  # on parcours tous les sommets
        for code_lien in noeud[
            "incidence"
        ]:  # double boucle : passe 2 fois par lien de la métropole si tout est correct : O(|E_metropole])
            if code_lien in dico_liens:  # si le lien est dans la région d'intéret
                dico_liens_graphe[code_lien] = dico_liens_graphe.get(
                    code_lien, dico_liens[code_lien].copy()
                )  # copy pour pas modifier le lien original et éviter les effets de bord
                dico_liens_graphe[code_lien]["extremites"] = dico_liens_graphe[
                    code_lien
                ].get("extremites", []) + [
                    id
                ]  # on mémorise que id est une extrémité du lien

    # les "bons" liens sont incidents à 2 sommets. On compte ceux qui ont trop d'extremites, pas assez ou pas du tout
    nb_liens_bugs = len(
        [
            code_lien
            for code_lien in dico_liens_graphe
            if len(dico_liens_graphe[code_lien]["extremites"]) > 2
        ]
    )
    nb_liens_deconnectes = len(
        [
            code_lien
            for code_lien in dico_liens_graphe
            if len(dico_liens_graphe[code_lien]["extremites"]) == 1
        ]
    )
    print(
        f"{nb_liens_bugs} ont trop d'extrémités, {nb_liens_deconnectes} n'en ont pas assez, {len(dico_liens)-len(dico_liens_graphe)} n'en ont pas"
    )

    return {
        code_lien: dico_liens_graphe[code_lien]
        for code_lien in dico_liens_graphe
        if len(dico_liens_graphe[code_lien]["extremites"]) == 2
    }  # generation du résultat : O(|E_quartier])


def construire_graphe(dico_noeuds, dico_liens_graphe):
    """
    dico_noeuds: dictionnaire contenant les noeuds de la métropole
    dico_liens_graphe: dictionnaire contenant les liens d'un quartier de la métropole ayant exactement 2 extrémités dans dico_noeuds et la liste des 2 extremités
    construit le graphe (noeuds, liens) et renvoie le dictionnaire
        - clé: les noeuds incidents à au moins un lien valide
        - valeurs : attributs du noeuds + dictionnaire des voisins dans le graphe: clé identifiant de noeud, valeur code du lien d'adjacence
    """
    dico_noeuds_graphe = {}
    for code_lien, lien in dico_liens_graphe.items():  # O(|E_quartier|)
        if len(lien.get("extremites", [])) == 2:
            [u, v] = lien["extremites"]
            noeud_u = dico_noeuds[u]
            dico_noeuds_graphe[u] = dico_noeuds_graphe.get(
                u,
                {
                    "voisins": dict(),
                    "incidence": [],
                    "nom": noeud_u["nom"],
                    "geometry": noeud_u["geometry"],
                },
            )
            noeud_v = dico_noeuds[v]
            dico_noeuds_graphe[v] = dico_noeuds_graphe.get(
                v,
                {
                    "voisins": dict(),
                    "incidence": [],
                    "nom": noeud_v["nom"],
                    "geometry": noeud_v["geometry"],
                },
            )
            dico_noeuds_graphe[u]["voisins"][v] = code_lien
            dico_noeuds_graphe[u]["incidence"].append(code_lien)
            dico_noeuds_graphe[v]["voisins"][u] = code_lien
            dico_noeuds_graphe[v]["incidence"].append(code_lien)
        else:
            print(f"bug {code_lien}, {lien}")

    return dico_noeuds_graphe


def changer_rep_graphe(noeuds_graphe):
    """Fonction qui transforme le graphe lu à partir du fichier Json dans le format du graphe utilisé dans l'exercice 5"""
    for noeud, dico_desc in noeuds_graphe.items():
        liste_voisins = list(dico_desc["voisins"].keys())
        dico_desc["voisins"] = liste_voisins


if __name__ == "__main__":

    fichier_noeuds = "data/metropole_noeuds.json"
    fichier_liens = "data/metropole-de-lyon_adr_voie_lieu.adraxevoie.json"

    liens = dictionnaire_liens(fichier_liens)
    noeuds = dictionnaire_noeuds(fichier_noeuds)

    print(len(noeuds), "noeuds (métropole) -----", len(liens), "liens (Villeurbanne)")

    liens_valides = selectionner_liens_graphe(
        noeuds, liens
    )  # garde que les "bons" liens du quartier et ajoute leurs extremités
    print(len(liens_valides), "bons liens")

    noeuds_graphe = construire_graphe(
        noeuds, liens_valides
    )  # construit le graphe des bons liens, y compris le voisinnage

    print(
        "Villeurbanne :",
        len(noeuds_graphe),
        "noeuds -----",
        len(liens_valides),
        "liens",
    )
    changer_rep_graphe(noeuds_graphe)
    plot_graphe(noeuds_graphe)
