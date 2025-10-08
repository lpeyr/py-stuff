#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:51:16 2023

@author: nadiaB
"""

import csv
import json


################
#Question 2.5
################            
def moyenne(l):
    s=0
    for v in l:
        s+=v
    return s/len(l)

def affiche_stats_matiere(dico_eleves,matiere):
    '''
      Fonction qui affiche les notes connues d'une matière ainsi que la moyenne de ces notes
     Args:
         dico_eleves, dictionnaire de tous les eleves
         matiere, matière pour laquelle on affiche les notes
     Return: None
     '''
    notes = []
    for eleves in dico_eleves.values():
        if matiere in eleves["notes"] and eleves["notes"][matiere] != "":
            notes.append(float(eleves["notes"][matiere]))
    print(f"Les notes de {matiere} sont : {notes}\nLa moyenne est {moyenne(notes)}")
    
 ################
#Question 2.6
################
def affiche_notes_eleve(dico_eleves,nom,prenom):
    ''' Fonction qui affiche les notes d'un eleve dont le nom et le prenom sont fournis
    Args:
        dico_eleve, Dictionnaire avec comme clé prenom,nom de l'eleve et comme 
        valeur le dictionnaire associé à cet eleve
        nom (chaine) : nom de l'eleve'
        prenom (chaine), prenom de l'eleve'
    Return: None
    '''
    print(dico_eleves[f"{prenom},{nom}"]["notes"].values())
     
 #############################################################################
 #  Code Fourni
 ############################################################################
 

def csv_to_dico_eleves_imbrique(nom_fichier, eliminer_entete=True, delimiteur=','):
    """
    fonction qui renvoie une liste dont chaque élément est une liste qui correspond à une ligne du fichier csv passé en paramèter
        Entrees: nom_fichier (string)
                eliminer_entete (booléen) : indique s'il faut éliminer la première ligne du fichier (par défaut True)
                delimiteur (char) : le délimiteur de colonne (par défaut ',')
        Sortie: la liste des listes des données du csv
    """
    with open(nom_fichier, 'r', encoding= 'utf-8') as f:
        csvReader = csv.reader(f, delimiter=delimiteur) #interprête le fichier comme un csv avec délimiteur
    #le fichier f est maintenant fermé
        dico_eleve = {}
        attributs = ['Ville','NumEtudiant']
        if eliminer_entete:
            csvReader.__next__() #passe la première ligne du csv si ce sont les entêtes
        
        for row in csvReader: #parcours toutes les lignes du csv
            np_eleve = row[1]+","+row[0]
            dico = dico_eleve.get(np_eleve,{})
            if dico == {}:
                dico['Ville'] = row[2]
                dico['NumEtudiant'] = row[3]
                dico["notes"] =  {}
            dico["notes"][row[4]] = row[5] 
             
            dico_eleve[np_eleve] = dico
             
        
    return dico_eleve

#programme principal

dico_eleves = csv_to_dico_eleves_imbrique('data/Resultat_requete.csv')
# si vous travaillez sous Windows
#liste_de_liste= csv_to_liste('data\Resultat_requete.csv')

print(dico_eleves)


#*****************
#    Exercice 2
#*****************

#########################
# Reponses aux questions 2.2 à 2.4
##########################
print(dico_eleves["George,SAND"])
print(dico_eleves["Jacques,PREVERT"]["notes"]["informatique"])
print(len(dico_eleves["Blaise,PASCAL"]["notes"].keys()))

# Décommenter chaque appel une fois la question traitée
# Q2.5
print(f'Question2.5: résultats')
affiche_stats_matiere(dico_eleves,'analyse 1')

print()


#Q2.6
print(f'Question2.6: résultats')
#######################
affiche_notes_eleve(dico_eleves,'PASCAL','Blaise')
print()



 

 

