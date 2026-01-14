def BFS_parents(s_init, adj):
    """
    Version du BFS où on construit tout le dictionnaire des parents
    Entrées : s_init sommet de départ, adj graphe
    Sortie : dictionnaire des parents
    """
    q = [s_init]
    visite = [s_init]
    parent = dict()
    while len(q) > 0:
        u = q.pop(0)
        for v in adj[u]["voisins"]:
            if v not in visite:
                q.append(v)
                visite.append(v)
                parent[v] = u
    return parent


# def calcul_chemin(s, dico_prec):
#     '''
#     Retourne le chemin qui va du noeud racine vers le noeud s à partir du dictionnaire des parents dico_prec
#     '''
#     chemin = []
#     file = [s]
#     while len(file) > 0:
#         u = file.pop(0)
#         if u in dico_prec:
#             chemin.append(dico_prec[u])
#             file.append(dico_prec[u])
#     return [] if len(chemin[::-1]) == 0 else chemin[::-1] + [s]
def calcul_chemin(s, dico_prec):
    """
    Retourne le chemin qui va du noeud racine vers le noeud s à partir du dictionnaire des parents dico_prec
    """
    if dico_prec.get(s, None) == None:
        return []
    else:
        return calcul_chemin(dico_prec[s], dico_prec) + [s]


def pf_le_pproche_parents(dico_parents, l_noms_nf):
    """
    Retourne le point de fraicheur de la liste l_noms_nf le plus proche de la racine en utilisant le dictionnaire des parents dico_parents
    """
    chemin = []
    n = l_noms_nf[0]
    for noeud in l_noms_nf:
        ch = calcul_chemin(noeud, dico_parents)
        if len(chemin) == 0 or len(ch) < len(chemin):
            chemin = ch
    return n


def BFS_hauteurs(s_init, adj):
    """
    BFS qui calcule le dictionnaire des hauteurs/distances en terme de nombre de liens depuis la racine s_init
    Entrées : s_init sommet de départ, adj graphe
    Sortie : dictionnaire des distances
    """
    hauteur = dict()
    hauteur[s_init] = 0
    q = [s_init]
    visite = [s_init]
    while len(q) > 0:
        u = q.pop(0)
        for v in adj[u]["voisins"]:
            if v not in visite:
                q.append(v)
                visite.append(v)
                hauteur[v] = hauteur.get(u, 0) + 1

    return hauteur


def pf_le_pproche(dico_hauteur, l_noms_nf):
    """
    Retourne le point de fraicheur de la liste l_noms_nf le plus proche de la racine en utilisant le dico des hauteurs dico_hauteur
    """
    nf = l_noms_nf[0]
    d_min = dico_hauteur[nf]
    for node in l_noms_nf:
        if dico_hauteur[node] < d_min:
            d_min = dico_hauteur[node]
            nf = node
    return nf


def BFS_avec_arret(s_init, adj, l_noms_nf):
    """
    Version du BFS qui s'arrete dès qu'un des points de friacheur est atteint
    Entrées : s_init sommet de départ, adj graphe, l_noms_nf liste des points de fraicheur
    Sortie : noeud de fraicheur le plus proche de s_init
    """
    q = [s_init]
    visite = [s_init]
    nf = None
    while len(q) > 0:
        u = q.pop(0)
        if u in l_noms_nf:
            return u
        for v in adj[u]["voisins"]:
            if v not in visite:
                q.append(v)
                visite.append(v)

    return nf


def BFS_meilleur_ancetre(s_init, adj, dico_ancetre):
    """
    Cette fonction applique le BFS en partant d'un noeud de fraicheur et calcule au fur et à mesure les hauteurs avec stockage du meilleur (ancetre) noeud de fraicheur.
    L'algo ne met pas dans la file d'attente les noeuds dont la distance aux noeuds de fraicheurs précedemment traités  est meilleure
    Ce BFS est lancé uniquement à partir des points de fraicheur
    Entrées : s_init sommet de départ, adj graphe, dico_ancetre dictionnaire stockant pour chaque noeud le meilleur ancetre + la distance
    Sortie : aucune. Le dictionnaire des ancetres est actualisé
    """
    dico_ancetre[s_init] = (None, 0)
    q = [s_init]
    while len(q) > 0:
        u = q.pop(0)
        distance = dico_ancetre[u][1]
        for v in adj[u]["voisins"]:
            if v not in dico_ancetre or distance + 1 < dico_ancetre[v][1]:
                q.append(v)
                dico_ancetre[v] = (u, distance + 1)
