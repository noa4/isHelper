import csv
from classes import *
from modeles import *
import sqlite3 as sql

class LectureDialect(csv.Dialect):
    #Séparateur de champ
    delimiter = ";"
    #Séparateur de chaîne
    quotechar = None
    #Gestion du séparateur dans les chaînes
    escapechar = None
    doublequote = None
    #Fin de ligne
    lineterminator = "\r\n"
    #Ajout automatique du séparateur de chaîne
    quoting = csv.QUOTE_NONE
    skipinitialspace = False

db = sql.connect('bdd.sql')
MgrBesoins = BesoinsMgr(db)


file = open("Classeur.csv","r")
besoin = csv.reader(file, LectureDialect)

def IsPrimaire(x):
    print(x)
    if len(x[(x.index(' ') + 1):]) > 1:
        return False
    return True

for row in besoin:
    MgrBesoins.create(row[1], primaire = IsPrimaire(row[0]))
