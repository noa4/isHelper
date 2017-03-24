# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 08:33:04 2016

@author: 2016-0308
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
            besoin INT,
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

MgrExigences = ExigencesMgr(db)
MgrBesoins = BesoinsMgr(db)
MgrPieces = PieceMgr(db)

liste_exigences = list()
liste_besoins = list()
nomenclature = list()

import tkinter as tk


def Renseigner_Aide():
    import tkinter as tk
    # récupération du type d'exigence
    fenetre = tk.Tk()
    label = tk.Label(fenetre, text="Il n'y en a pas", bg="red")
    label.pack()
    fenetre.mainloop()


def Renseigner_Exigence():
    import tkinter as tk
    # récupération du type d'exigence
    fen = tk.Toplevel(fenetre)

    def CreerExigence():
        print(exigence_mere.get())
        MgrExigences.create(intitule.get(), critere.get(), besoin=int(besoin_origine.get()), espece=int(value.get()), niveau=int(niveau.get()),
                            exigence_mere=int(exigence_mere.get()))
        fen.destroy()

    def DemanderExigenceMere():
        if int(mere.get()) == True:
            fen1 = tk.Toplevel(fen)
            for i in MgrExigences.read():
                tk.Radiobutton(fen1, text=str(i.idex), variable=exigence_mere, value=i.idex).pack()
            tk.Button(fen1, text="Valider", command=CreerExigence).pack()
        # print(intitule.get())
        #            print(critere.get())
        #            print(value.get())
        #            print(niveau.get())
        else:
            MgrExigences.create(intitule.get(), critere.get(), besoin=int(besoin_origine.get()), espece=int(value.get()), niveau=int(niveau.get()),
                                exigence_mere=0)
            fen.destroy()



    def Valider():
        fen2 = tk.Toplevel(fen)
        # récupération de l'intitulé de l'exigence
        txt1 = tk.Label(fen2, text='Intitulé :')
        entree0 = tk.Entry(fen2, textvariable=intitule, width=100)
        # récupération de la caractéristique de l'exigence
        txt2 = tk.Label(fen2, text='Caractéristique :')
        entree1 = tk.Entry(fen2, textvariable=critere, width=30)
        # récupération du niveau du critère
        txt3 = tk.Label(fen2, text='Niveau du critère :')
        entree2 = tk.Entry(fen2, textvariable=niveau, width=30)
        # récupération de la caratéristique mère
        txt4 = tk.Label(fen2, text='Exigence mère :')
        bouton4_1 = tk.Radiobutton(fen2, text="Oui", variable=mere, value=1)
        bouton4_2 = tk.Radiobutton(fen2, text="Non", variable=mere, value=0)
        #Récupération beoin lié
        txt5 = tk.Label(fen2, text='Besoin lié :')

        txt1.grid(row=0)
        txt2.grid(row=1)
        txt3.grid(row=2)
        txt4.grid(row=3)
        entree0.grid(row=0, column=1)
        entree1.grid(row=1, column=1)
        entree2.grid(row=2, column=1)
        bouton4_1.grid(row=3, column=1, )
        bouton4_2.grid(row=3, column=2)
        txt5.grid(row=4)
        for i in MgrBesoins.read():
            tk.Radiobutton(fen2, text=str(i.id_besoin), variable=besoin_origine, value=i.id_besoin).grid(column =1)
        print(besoin_origine.get())
        # Bouton de sortie
        bouton4 = tk.Button(fen2, text="Valider", command=DemanderExigenceMere)
        bouton4.grid(column = 1)

    bouton1 = tk.Radiobutton(fen, text="Fonctionnelle", variable=value, value=1)
    bouton2 = tk.Radiobutton(fen, text="Non Fonctionnelle", variable=value, value=0)
    bouton3 = tk.Button(fen, text="Valider", command=Valider)
    bouton1.pack()
    bouton2.pack()
    bouton3.pack()


def Renseigner_Besoin():
    import tkinter as tk
    #mise à jour du menu( permettre ajout exigence)

    # récupération du type de besoin
    fen = tk.Toplevel(fenetre)

    def CreerBesoin():
        MgrBesoins.create(intitule1.get(), int(value.get()))
        #        print(intitule1.get())
        #        print(value.get())
        tkupdate()
        fen.destroy()

    def Valider():
        fen2 = tk.Toplevel(fen)
        # récupération de l'intitulé du besoin
        txt1 = tk.Label(fen2, text='Intitulé :')
        entree0 = tk.Entry(fen2, textvariable=intitule1, width=100)
        # Bouton de sortie
        bouton4 = tk.Button(fen2, text="Valider", command=CreerBesoin)
        txt1.grid(row=0)
        entree0.grid(row=0, column=1)
        bouton4.grid(row=3, column=1)

    bouton1 = tk.Radiobutton(fenetre, text="Besoin Primaire", variable=value, value=1)
    bouton2 = tk.Radiobutton(fenetre, text="Besoin Secondaire", variable=value, value=0)
    bouton3 = tk.Button(fenetre, text="Valider", command=Valider)
    bouton1.pack()
    bouton2.pack()
    bouton3.pack()


def Renseigner_Piece():
    import tkinter as tk
    # récupération du type de besoin
    fen = tk.Toplevel(fenetre)

    def CreerPiece():
        MgrPieces.create(nom_piece.get(), couleur.get())
        #        print(nom_piece.get())
        #        print(couleur.get())
        fen.destroy()

    txt1 = tk.Label(fen, text='Nom de la pièce :')
    entree1 = tk.Entry(fen, textvariable=nom_piece, width=50)
    txt2 = tk.Label(fen, text='Couleur :')
    entree2 = tk.Entry(fen, textvariable=couleur, width=50)
    bouton1 = tk.Button(fen, text="Valider", command=CreerPiece)
    txt1.pack()
    entree1.pack()
    txt2.pack()
    entree2.pack()
    bouton1.pack()


def Del_Exigence():
    import tkinter as tk
    fen = tk.Toplevel(fenetre)

    def Valider():
        MgrExigences.delete(nom_exigence)
        fen.destroy()

    for i in MgrExigences.read():
        texte = str(i.idex)
        tk.Radiobutton(fen, text=texte, variable=nom_exigence, value=i.idex).pack()
    tk.Button(fen, text="Valider", command=Valider).pack()


def Del_Besoin():
    import tkinter as tk
    fen = tk.Toplevel(fenetre)

    def Valider():
        MgrBesoins.delete(nom_besoin)
        fen.destroy()

    for i in MgrBesoins.read():
        texte = str(i.id_besoin)
        tk.Radiobutton(fen, text=texte, variable=nom_besoin, value=i.id_besoin).pack()
    tk.Button(fen, text="Valider", command=Valider).pack()


def Del_Piece():
    import tkinter as tk
    fen = tk.Toplevel(fenetre)

    def Valider():
        MgrPieces.delete(nom_piece)
        fen.destroy()

    for i in MgrPieces.read():
        texte = str(i.nom)
        tk.Radiobutton(fen, text=texte, variable=nom_piece, value=i.nom).pack()
    tk.Button(fen, text="Valider", command=Valider).pack()


def Modifier_Exigence():
    fen = tk.Toplevel(fenetre)

    def Update():
        MgrExigences.read(int(nom_exigence.get())).intitule = intitule.get()
        MgrExigences.read(int(nom_exigence.get())).critere = critere.get()
        MgrExigences.read(int(nom_exigence.get())).besoin = besoin_origine.get()
        MgrExigences.read(int(nom_exigence.get())).espece = value.get()
        MgrExigences.read(int(nom_exigence.get())).niveau = niveau.get()
        MgrExigences.update(MgrExigences.read(int(nom_exigence.get())))
        fen.destroy()

    def Valider():
        # récupération de l'intitulé de l'exigence
        txt1 = tk.Label(fen, text='Intitulé :')
        entree0 = tk.Entry(fen, textvariable=intitule, width=100)
        # récupération de la caractéristique de l'exigence
        txt2 = tk.Label(fen, text='Caractéristique :')
        entree1 = tk.Entry(fen, textvariable=critere, width=30)
        # récupération du niveau du critère
        txt3 = tk.Label(fen, text='Niveau du critère :')
        entree2 = tk.Entry(fen, textvariable=niveau, width=30)
        # Récupération beoin lié
        txt5 = tk.Label(fen, text='Besoin lié :')

        txt1.grid(row=0)
        txt2.grid(row=1)
        txt3.grid(row=2)
        entree0.grid(row=0, column=1)
        entree1.grid(row=1, column=1)
        entree2.grid(row=2, column=1)
        txt5.grid(row=4)
        for i in MgrBesoins.read():
            tk.Radiobutton(fen, text=str(i.id_besoin), variable=besoin_origine, value=i.id_besoin).pack()
        print(besoin_origine.get())
        # Bouton de sortie
        bouton4 = tk.Button(fen, text="Valider", command=Update)
        bouton4.pack()

    tk.Label(fen, text ="Identifiant de l'exigence à modifier: ").pack()
    for i in MgrExigences.read():
        texte = str(i.idex)
        tk.Radiobutton(fen, text=texte, variable=nom_exigence, value=i.idex).pack()
    tk.Button(fen, text="Valider", command=Valider).pack()

def Modifier_Besoin():
    fen = tk.Toplevel(fenetre)

    def Update():
        MgrBesoins.read(int(nom_besoin.get())).intitule = intitule1.get()
        MgrBesoins.read(int(nom_besoin.get())).primaire = int(value.get())
        MgrBesoins.update(MgrBesoins.read(int(nom_besoin.get())))
        fen.destroy()

    def Valider():
        # récupération de l'intitulé du besoin
        txt1 = tk.Label(fen, text='Intitulé :')
        entree0 = tk.Entry(fen, textvariable=intitule1, width=100)
        txt1.grid(row=0)
        entree0.grid(row=0, column=1)
        tk.Radiobutton(fen, text="Besoin Primaire", variable=value, value=1).pack()
        tk.Radiobutton(fen, text="Besoin Secondaire", variable=value, value=0).pack()
        tk.Button(fen, text="Valider", command=Update).pack()

    tk.Label(fen, text="Identifiant du besoin à modifier: ").pack()
    for i in MgrBesoins.read():
        texte = str(i.id_besoin)
        tk.Radiobutton(fen, text=texte, variable=nom_besoin, value=i.id_besoin).pack()
    tk.Button(fen, text="Valider", command=Valider).pack()

def Modifier_Piece():
    fen = tk.Toplevel(fenetre)

    def Update():
        # Mise à jour des variables
        MgrPieces.read(int(nom_piece.get())).nom = intitule_piece.get()
        MgrPieces.read(int(nom_piece.get())).couleur = couleur.get()
        MgrPieces.update(MgrPieces.read(int(nom_piece.get())))
        fen.destroy()

    def Valider():
        tk.Label(fen, text='Nom de la pièce :').pack()
        tk.Entry(fen, textvariable=intitule_piece, width=50).pack()
        tk.Label(fen, text='Couleur :').pack()
        tk.Entry(fen, textvariable=couleur, width=50).pack()
        tk.Button(fen, text="Valider", command=Update).pack()

    tk.Label(fen, text="Identifiant de la pièce à modifier: ").pack()
    for i in MgrPieces.read():
        texte = str(i.id_piece)
        tk.Radiobutton(fen, text=texte, variable=nom_piece, value=i.id_piece).pack()
    tk.Button(fen, text="Valider", command=Valider).pack()

def RenseignerGantt():
    import datetime
    import gantt
    import tkinter as tk
    fenetre2 = tk.Toplevel(fenetre)

    def Renseigner_Projet():
        fen = tk.Toplevel(fenetre2)

        def Valider():
            liste_projet.append(gantt.Project(name=nom_projet.get()))
            fen.destroy()

        tk.Label(fen, text='Intitulé du projet :').pack()
        tk.Entry(fen, textvariable=nom_projet, width=100).pack()
        tk.Button(fen, text="Valider", command=Valider).pack()

    def Renseigner_Personnel():
        fen = tk.Toplevel(fenetre2)

        def Valider():
            liste_personne.append(gantt.Resource(nom_personne.get()))
            fen.destroy()

        tk.Label(fen, text="Nom du personnel :").pack()
        tk.Entry(fen, textvariable=nom_personne, width=100).pack()
        tk.Button(fen, text="Valider", command=Valider).pack()

    def Ajouter_Tache_Projet():
        fen = tk.Toplevel(fenetre2)

        def Valider():
            liste_projet[int(projet.get())].add_task(liste_tache[int(tache.get())])
            fen.destroy()

        for i in range(len(liste_projet)):
            tk.Radiobutton(fen, text=str(i + 1), variable=projet, value=i).pack()
        for i in range(len(liste_tache)):
            tk.Radiobutton(fen, text=str(i + 1), variable=tache, value=i).pack()
        tk.Button(fen, text="Valider", command=Valider).pack()

    def Renseigner_Tache():
        fen = tk.Toplevel(fenetre2)

        def Valider():
            liste_tache.append(gantt.Task(name=nom_tache.get(),
                                          start=datetime.date(int(start.get()[6:10]), int(start.get()[3:5]),
                                                              int(start.get()[:2])), duration=int(temps.get()),
                                          percent_done=int(pourcentage.get()),
                                          resources=[liste_personne[int(nom.get())]]))
            fen.destroy()

        tk.Label(fen, text="Intitulé de la tache :").pack()
        tk.Entry(fen, textvariable=nom_tache, width=100).pack()
        tk.Label(fen, text='''Date de début forme jj/mm/aaaa :''').pack()
        tk.Entry(fen, textvariable=start, width=100).pack()
        tk.Label(fen, text='''Durée de la tache :''').pack()
        tk.Entry(fen, textvariable=temps, width=100).pack()
        for i in range(len(liste_personne)):
            tk.Radiobutton(fen, text=liste_personne[i].fullname, variable=nom, value=i).pack()
        tk.Label(fen, text='''Avance (pourcentage) :''').pack()
        tk.Entry(fen, textvariable=pourcentage, width=100).pack()
        tk.Button(fen, text="Valider", command=Valider).pack()

    def Afficher_diagramme():
        fen = tk.Toplevel(fenetre2)

        def Valider():
            liste_projet[int(projet.get())].make_svg_for_tasks(filename=nom_diagramme.get() + '.svg',
                                                               today=datetime.date(int(today.get()[6:10]),
                                                                                   int(today.get()[3:5]),
                                                                                   int(today.get()[:2])),
                                                               start=datetime.date(int(start.get()[6:10]),
                                                                                   int(start.get()[3:5]),
                                                                                   int(start.get()[:2])),
                                                               end=datetime.date(int(end.get()[6:10]),
                                                                                 int(end.get()[3:5]),
                                                                                 int(end.get()[:2])))
            fen.destroy()

        for i in range(len(liste_projet)):
            tk.Radiobutton(fen, text=str(i + 1), variable=projet, value=i).pack()
        tk.Label(fen, text='''Date d'aujourd'hui forme jj/mm/aaaa :''').pack()
        tk.Entry(fen, textvariable=today, width=100).pack()
        tk.Label(fen, text='''Date de début diagramme :''').pack()
        tk.Entry(fen, textvariable=start, width=100).pack()
        tk.Label(fen, text='''Date de fin diagramme :''').pack()
        tk.Entry(fen, textvariable=end, width=100).pack()
        tk.Label(fen, text='''Nom du diagramme :''').pack()
        tk.Entry(fen, textvariable=nom_diagramme, width=100).pack()
        tk.Button(fen, text="Valider", command=Valider).pack()

    # Définition des menus
    menubarG = tk.Menu(fenetre2)

    menuG = tk.Menu(menubarG, tearoff=0)
    menuG.add_command(label="Renseigner Projet", command=Renseigner_Projet)
    menuG.add_command(label="Renseigner Personnel", command=Renseigner_Personnel)
    menuG.add_command(label="Renseigner Tache", command=Renseigner_Tache)
    menuG.add_command(label="Ajouter Tache au projet", command=Ajouter_Tache_Projet)
    menuG.add_separator()
    menuG.add_command(label="Quitter", command=fenetre2.destroy)
    menubarG.add_cascade(label="Fichier", menu=menuG)

    menuG = tk.Menu(menubarG, tearoff=0)
    menuG.add_command(label="Visualisation", command=Afficher_diagramme)
    menubarG.add_cascade(label="Affichage", menu=menuG)

    fenetre2.config(menu=menubarG)


import tkinter as tk

def tkupdate():
    if len(MgrBesoins.read()) > 0:
        menubar.delete(0, 1)
        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Renseigner Besoin", command=Renseigner_Besoin)
        menu1.add_command(label="Renseigner Exigence", command=Renseigner_Exigence)
        menu1.add_command(label="Renseigner Piece", command=Renseigner_Piece)
        menu1.add_command(label="Modifier Exigence", command=Modifier_Exigence)
        menu1.add_command(label="Modifier Besoin", command=Modifier_Besoin)
        menu1.add_command(label="Modifier Piece", command=Modifier_Piece)
        menu1.add_command(label='Supprimer Exigence', command=Del_Exigence)
        menu1.add_command(label='Supprimer Besoin', command=Del_Besoin)
        menu1.add_command(label='Supprimer Pièce', command=Del_Piece)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=fenetre.destroy)
        menubar.insert_cascade(0, label='Gérer', menu=menu1)

def Fenetre_acceuil():
    fenetre.configure(background='#2c3e50')
    fenetre.title("IsHelper")
    logo = tk.PhotoImage(file="ish.gif")
    pic = tk.Label(fenetre, image=logo, bg='#2c3e50')
    pic.pack()
    # message d'accueil
    hometxt = "La solution d'aide à l'ingénierie système"
    text = tk.Label(fenetre, text=hometxt, bg='#2c3e50', fg='#ecf0f1', font=('Helvetica', 18))
    text.pack()

fenetre = tk.Tk()
Fenetre_acceuil()

menubar = tk.Menu(fenetre)

value = tk.StringVar()
# Exigence
intitule = tk.StringVar()
critere = tk.StringVar()
niveau = tk.StringVar()
mere = tk.StringVar()
exigence_mere = tk.StringVar()
nom_exigence = tk.StringVar()
besoin_origine = tk.StringVar(None)
# Besoin
intitule1 = tk.StringVar()
nom_besoin = tk.StringVar()
# Pièce
nom_piece = tk.StringVar()
couleur = tk.StringVar()
intitule_piece = tk.StringVar()
# Projet
nom_projet = tk.StringVar()
liste_projet = list()
# Equipe humaine
nom_personne = tk.StringVar()
liste_personne = list()
# Tache
nom_tache = tk.StringVar()
tache = tk.StringVar()
temps = tk.StringVar()
nom = tk.StringVar()
pourcentage = tk.StringVar()
liste_tache = list()
# Affichage (définition des dates)
projet = tk.StringVar()
today = tk.StringVar()
start = tk.StringVar()
end = tk.StringVar()
nom_diagramme = tk.StringVar()

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Renseigner Besoin", command=Renseigner_Besoin)
menu1.add_command(label="Renseigner Exigence", state='disabled', command=Renseigner_Exigence)
menu1.add_command(label="Renseigner Piece", command=Renseigner_Piece)
menu1.add_command(label="Modifier Exigence", command=Modifier_Exigence)
menu1.add_command(label="Modifier Besoin", command=Modifier_Besoin)
menu1.add_command(label="Modifier Piece", command=Modifier_Piece)
menu1.add_command(label='Supprimer Exigence', command=Del_Exigence)
menu1.add_command(label='Supprimer Besoin', command=Del_Besoin)
menu1.add_command(label='Supprimer Pièce', command=Del_Piece)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Gérer", menu=menu1)

menu2 = tk.Menu(menubar, tearoff=0)
menu2.add_command(label="Couper")
menu2.add_command(label="Copier")
menu2.add_command(label="Coller")
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = tk.Menu(menubar, tearoff=0)
menu3.add_command(label="Gantt", command=RenseignerGantt)
menubar.add_cascade(label="Diagramme", menu=menu3)

menu4 = tk.Menu(menubar, tearoff=0)
menu4.add_command(label="A propos", command=Renseigner_Aide)
menubar.add_cascade(label="Aide", menu=menu4)

fenetre.config(menu=menubar)

#test si la bdd ouverte permet l'ajout d'exigences
tkupdate()

fenetre.mainloop()



