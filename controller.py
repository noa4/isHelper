# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 08:40:48 2017

@author: 2016-0687
"""
from classes import *
from modeles import *
import sqlite3 as sql
db = sql.connect('bdd.sql')
'''
cursor = db.cursor()
cursor.execute("""CREATE TABLE pieces(
            id_piece INTEGER PRIMARY KEY,
            nom_piece TEXT,
            couleur INTEGER); """)
cursor.execute("""CREATE TABLE exigences(
            idex INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            origine TEXT,
            intitule TEXT,
            critere TEXT,
            espece INTEGER,
            niveau INT,
            resultat INT,
            conclusion INT,
            exigence_mere INTEGER); """)
cursor.execute("""CREATE TABLE systeme(
            id_systeme INTEGER PRIMARY KEY,
            exigences TEXT,
            caracteristique TEXT); """)
cursor.execute("""CREATE TABLE besoins(
            id_besoin INTEGER PRIMARY KEY,
            intitule TEXT,
            primaire INTEGER); """)
cursor.execute("""CREATE TABLE testresults(
            idex INTEGER PRIMARY KEY,
            critere TEXT,
            niveau INT);""")
db.commit()

'''
"""
b = Exigence(3,'doit poser la pièce', '5%',0)
c = Exigence(8,'doit déplacer la pièce', '10%',1)
d = Exigence(4,'doit capter la couleur de la pièce', '15%')
"""

mgr = ExigencesMgr(db)
a = mgr.create('doit lever la pièce','bras metallique',1,'3%',13)
print(a)