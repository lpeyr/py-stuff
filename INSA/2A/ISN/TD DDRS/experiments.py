import json
from random import randint
import BFS_algos
import time
import courbes


def lire_graphe(nom_fichier):
    '''Fonction qui lit le fichier json dont le nom est fourni en paramètre et retourne un dictionnaire 
    representant le graphe'''
    with open(nom_fichier, "r", encoding="utf-8") as f:
        graphe_noeuds = json.load(f)
    return graphe_noeuds

def init_affectation(l_noms_nf):
    """Fonction qui construit un dico ayant pour clé les noeuds de fraicheur et pour valeurs la 
    liste vide pour initialiser les ensembles d'habitants qui se rendent à chaque point de fraicheur"""
    deploy = {}
    for nom_noeud in l_noms_nf:
         deploy[nom_noeud] = []
    return deploy

def choisir_points_fraicheur(dico_graphe,n):
   '''Fonction qui choisit aléatoirement 'n' poin,t de fraicheurs parmi les noeuds du graphe'''
   liste_noeuds = list(dico_graphe.keys()) 
   l_noms_nf = []
   while len(l_noms_nf) <n:
       rdm = randint(0,len(liste_noeuds)-1)
       if liste_noeuds[rdm] not in l_noms_nf:
           l_noms_nf.append(liste_noeuds[rdm])
   return l_noms_nf

         
###############################################
#     Algo 1
###############################################      
# def BFS_complet_pour_tout_h(l_noms_nf, graphe):
#    '''
#    Exécute depuis chaque noeud representant des habitants un parcours BFS, puis détermine le point de fraicheur le plus proche en utilisant le dictionnaire des parents
#    Entrées : l_noms_nf (liste des noeuds de fraicheur), graphe
#    Sortie : dictionnaire des affectations associant chaque noeud de fraicheur à la liste des noeuds habitant s'y rendant
#    '''   
#    deploy = init_affectation(l_noms_nf) 
#    for node in graphe:
#        chemin = []
#        fr_min = l_noms_nf[0]
#        for fraicheur in l_noms_nf:
#            parents = BFS_algos.BFS_parents(fraicheur, graphe)
#            ch = BFS_algos.calcul_chemin(node, parents)
#            if len(chemin) == 0 or len(ch) < len(chemin):
#                chemin = ch.copy()
#                fr_min = fraicheur
#        deploy[fr_min].append(node)
#        
#    return deploy
#  
def BFS_complet_pour_tout_h(l_noms_nf, graphe):
    '''
    Exécute depuis chaque noeud representant des habitants un parcours BFS, puis détermine le point de fraicheur le plus proche en utilisant le dictionnaire des parents
    Entrées : l_noms_nf (liste des noeuds de fraicheur), graphe
    Sortie : dictionnaire des affectations associant chaque noeud de fraicheur à la liste des noeuds habitant s'y rendant
    '''   
    deploy = init_affectation(l_noms_nf) 
    for node in graphe:
        if node in deploy:
            continue
        parents = BFS_algos.BFS_parents(node, graphe)
        nf = BFS_algos.pf_le_pproche_parents(parents, l_noms_nf)
        deploy[nf].append(node)

    return deploy

#############################################
#     Algo2
############################################### 

def BFS_complet_pour_tout_h_avec_calcul_distance(l_noms_nf, graphe):
    '''
    Exécute depuis chaque noeud representant des habitants un parcours BFS, puis détermine le point de fraicheur le plus proche en utilisant le dictionnaire des hauteurs
    Entrées : l_noms_nf (liste des noeuds de fraicheur), graphe
    Sortie : dictionnaire des affectations associant chaque noeud de fraicheur à la liste des noeuds habitant s'y rendant
    '''
    
    deploy = init_affectation(l_noms_nf)
    
    #A completer
    
    return deploy

       
           
#############################################
#     Algo3
############################################### 

def BFS_pour_tout_h_avec_arret_des_prem_nf(l_noms_nf, graphe):
    '''
    Exécute depuis chaque noeud representant des habitants un parcours BFS qui s'interrompt quand il trouve le point de fraicheur le plus proche et le renvoie
    Entrées : l_noms_nf (liste des noeuds de fraicheur), graphe
    Sortie : dictionnaire des affectations associant chaque noeud de fraicheur à la liste des noeuds habitant s'y rendant
    '''
    deploy =  init_affectation(l_noms_nf)
    
    #A completer
    
    return deploy


#############################################
#     Algo4
###############################################     
def BFS_complet_pour_tout_nf(l_noms_nf, graphe):
    '''
    Exécute depuis chaque noeud de fraicheur le parcours BFS contruisant le dictionnaire des hauteurs puis recherche, pour chaque noeud habitant, le pt de fraicheur le plus proche
    Entrées : l_noms_nf (liste des noeuds de fraicheur), graphe
    Sortie : dictionnaire des affectations associant chaque noeud de fraicheur à la liste des noeuds habitant s'y rendant
    '''
    deploy =  init_affectation(l_noms_nf)
    
    #A completer
    
    return deploy

   
         
 #############################################
 #     Algo5
 ###############################################  
    
def BFS_elague_pour_tout_nf(l_noms_nf, graphe):
    '''
    Exécute depuis chaque noeud de fraicheur le parcours BFS mettant à jour le dictionnaire des ancetres, puis associe chaque noeud habitant au pt de fraicheur le plus proche
    Entrées : l_noms_nf (liste des noeuds de fraicheur), graphe
    Sortie : dictionnaire des affectations associant chaque noeud de fraicheur à la liste des noeuds habitant s'y rendant
    '''
    
    deploy =  init_affectation(l_noms_nf)
    
    #A completer
            
    return deploy

#############################################
#     Programme principal
############################################### 
if __name__ == "__main__":

    noms_graphes = ['G_rayon0_25','G_rayon0_5','G_rayon1_0','G_rayon2_0','G_rayon2_5','G_rayon3_0','G_rayon6_0']
    algos = ["algo1","algo2","algo3","algo4","algo5"]

    nb_pts_fraich = 3 #nombre de pts de fraicheurs tirés aléatoirement (< 12)
    nb_repet = 10 #nombre de répétitions des expérimentations pour calculer une moyenne sur les tirages aléatoires

    nb_noeuds = [] #pour stocker le nombre de noeuds dans chaque graphe
    tps_calcul_algo1= [] #pour stocker les temps d'exécutation pour chaque graphe avec l'algo 1
    tps_calcul_algo2 = [] #avec l'algo 2
    tps_calcul_algo3 = [] #avec l'algo 3
    tps_calcul_algo4 = [] #avec l'algo 4
    tps_calcul_algo5 = [] #avec l'algo 5

    for nom in noms_graphes:
        dico_graphe = lire_graphe("G_tests/"+ nom +".json")
        liste_noeuds = list(dico_graphe.keys()) 
        nb_noeuds.append(len(liste_noeuds))
                
        #exécution des algortihmes
        for algo in algos:
            if algo == "algo1": 
                print("exec de l'algo 1 : solution utilisant BFS avec arbre des parents")
                tmps = 0
                for _ in range(nb_repet): #répétitions des expérimentations
                    l_noeuds_fraicheur = choisir_points_fraicheur(dico_graphe, nb_pts_fraich) #tirage aléatoire des pts de fraicheur
                    start = time.perf_counter()
                    deploy = BFS_complet_pour_tout_h(l_noeuds_fraicheur, dico_graphe)
                    end = time.perf_counter()
                    tmps += end-start
                tps_calcul_algo1.append(tmps/nb_repet)
            elif algo == "algo2":
                print("exec de l'algo 2 : solution utilisant BFS avec calcul des hauteurs")
                tmps = 0
                for _ in range(nb_repet):
                    l_noeuds_fraicheur = choisir_points_fraicheur(dico_graphe, nb_pts_fraich)
                    start = time.perf_counter()
                    deploy = BFS_complet_pour_tout_h_avec_calcul_distance(l_noeuds_fraicheur, dico_graphe)
                    end = time.perf_counter()
                    tmps += end-start
                tps_calcul_algo2.append(tmps/nb_repet)
            elif algo == "algo3":
                print("exec de l'algo 3 : solution utilisant BFS avec arret des atteinte du premier neoud de fraicheur ")
                tmps = 0
                for _ in range(nb_repet):
                    l_noeuds_fraicheur = choisir_points_fraicheur(dico_graphe, nb_pts_fraich)
                    start = time.perf_counter()
                    deploy = BFS_pour_tout_h_avec_arret_des_prem_nf(l_noeuds_fraicheur, dico_graphe)
                    end = time.perf_counter()
                    tmps += end-start
                tps_calcul_algo3.append(tmps/nb_repet)
            elif algo == "algo4" : 
                print("exec de l'algo 4 : solution utilisant BFS à partir des noeuds de fraicheur")
                tmps = 0
                for _ in range(nb_repet):
                    l_noeuds_fraicheur = choisir_points_fraicheur(dico_graphe, nb_pts_fraich)
                    start = time.perf_counter()
                    deploy = BFS_complet_pour_tout_nf(l_noeuds_fraicheur, dico_graphe)
                    end = time.perf_counter()
                    tmps += end-start
                tps_calcul_algo4.append (tmps/nb_repet)
            else:
                print("exec de l'algo 5: solution  utilisant le BFS meilleur ancetre")
                tmps = 0
                for _ in range(nb_repet):
                    l_noeuds_fraicheur = choisir_points_fraicheur(dico_graphe, nb_pts_fraich)
                    start = time.perf_counter()
                    deploy = BFS_elague_pour_tout_nf(l_noeuds_fraicheur, dico_graphe)
                    end = time.perf_counter()
                    tmps += end-start
                tps_calcul_algo5.append (tmps/nb_repet)
        
            print(f"Temps d'exécution moyen : {tmps/nb_repet:.5f} secondes pour {len(dico_graphe.keys())} noeuds")
            
    #tracer les courbes
    courbes.tracer_perf(nb_noeuds, tps_calcul_algo1, tps_calcul_algo2, tps_calcul_algo3, tps_calcul_algo4,tps_calcul_algo5)



        

        
