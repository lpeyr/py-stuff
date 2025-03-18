# -*- coding: UTF-8 -*-
from icalendar import Calendar, Event
import requests
from datetime import datetime, timezone, timedelta

#############################
##### FOURNI AUX ELEVES #####
#############################
def aujourdhui():
  '''Renvoie la date du jour (datetime)'''
  return datetime.utcnow()

def creer_date(annee, mois, jour):
  '''Renvoie la date correspondant au jour/mois/annee donnés en paramètres'''
  return datetime(annee, mois, jour, tzinfo=timezone.utc)

def lundi_de_la_semaine(date):
  '''Renvoie la date du lundi de la semaine de la date envoyée en paramètre'''
  return date - timedelta(days = date.weekday(), hours = date.hour)

def ajouter_jours(date, jours):
  '''Etant donné une date en entrée, renvoie la date correspondant à celle-ci + le nombre de jours passé en paramètre'''
  return date + timedelta(days=jours)


def creer_calendrier_url(url):
  '''Initialise un calendrier à partir d'une URL qui pointe vers un fichier ICS'''
  return Calendar.from_ical(requests.get(url).text)


def liste_evenements(calendrier, date_debut, date_fin):
  '''Etant donné un calendrier, une date de début et une date de fin, renvoie la liste des événements compris entre ces deux dates'''
  evenements = []
  for component in calendrier.walk():
    if component.name == "VEVENT":
      date_evenement = component.get('dtstart').dt
      if date_debut.timestamp() <= date_evenement.timestamp() and date_evenement.timestamp() <= date_fin.timestamp():
        evenements.append(component)
  return evenements

def extraire_titre(evenement):
  '''Renvoie le titre  d'un événement'''
  return str(evenement.get('summary'))

def extraire_duree(evenement):
  '''Renvoie la durée (nombres de secondes) d'un événement'''
  duree = evenement.get('dtend').dt - evenement.get('dtstart').dt
  return duree.total_seconds()

def extraire_description(evenement):
  '''Renvoie la description d'un événement'''
  return str(evenement.get('description'))


def contient_chaine(chaine, titre):
  ''' Renvoie True si la chaine de caractère titre contient la chaine de caractères chaine, False sinon'''
  return chaine in titre

def split_lines(chaine):
    ''' Découpe la chaine de caractères chaine selon les retours à la
    ligne (notés :\n) et stocke chaque bout de chaine dans une liste. Cette fonction renvoie
    donc une liste de chaines de caractères.'''
    return chaine.splitlines();
