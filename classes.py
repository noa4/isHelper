# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


class Besoin:
    def __init__(self, id_besoin, intitule, primaire=False):
        self.id_besoin = id_besoin
        self.primaire = primaire  # besoin primaire
        self.intitule = intitule

    def id_besoin(self):
        return self.id_besoin

    def primaire(self):
        return self.primaire

    def intitule(self):
        return self.intitule


class Exigence:

    def __init__(self, idex, intitule, critere, besoin=None, espece = 0,niveau=None, exigence_mere = 0):
        self.idex = idex
        self.exigence_mere = exigence_mere
        self.critere = critere
        self.espece = espece
        #Pour une exigence fonctionnelle vaut 1 sinon vaut 0
        self.besoin = besoin
        #Le besoin dont découle l'exigence
        self.intitule = intitule
        self.niveau = niveau

    def __str__(self):
        espece = "non fonctionnelle"
        if self.espece == 1:
            espece = "fonctionnelle"
        return "L'exigence N{} {} est une exigence {} d'intitulé {} ".format(self.idex, self.critere, espece,
                                                                             self.intitule)


class Piece():
    def __init__(self, id_piece, nom, couleur, quantite):
        self._nom = nom
        self.couleur = couleur
        self.id_piece = id_piece
        self.quantite = quantite


class Nomenclature():
    def __init__(self):
        self.liste_nomenclature = list()
        self.liste_piece_modele = list()

    def AddPiece(self, piece):
        if isinstance(piece, Piece):
            for i in self.liste_nomenclature:
                if i.id_piece == piece.id_piece:
                    return 'La pièce existe déjà'
            self.liste_nomenclature.append(piece)

    def __lecture_lxfml(self, nom):
        """
        En entrée le nom du fichier à lire format string
        Retourne la liste des pièces utilisées dans le modèle
        """
        from lxml import etree
        l = []
        tree = etree.parse("Z:/Config/Bureau/" + nom + ".lxfml")
        for brick in tree.xpath('/LXFML/Bricks/Brick'):
            l.append((brick.get("itemNos")))
        return l

    def Pieces_modele(self, liste):
        """
        Retourne la liste des pièces du modèle sous la forme d'une liste
        """
        l = []
        for i in liste:
            k = 0
            while k < len(l):
                if l[k][0] == i:
                    l[k][1] += 1
                    break
                k += 1
            if k == len(l):
                l.append([i, 1])
        for i in l:
            self.liste_piece_modele.append(Piece(i[0], i[1], i[2], i[4]))

    def extractionNomenclature(self, fichier):
        """retourne la liste des pièces de la nomenclature
        le fichier est stocké sur le bureau"""
        import csv
        f = open("Z:/Config/Bureau/" + fichier + ".csv", "r", encoding='latin1')
        cr = csv.reader(f)
        for row in cr:
            if row[0][0] != 'I':
                a = row[0].split(";", 4)
                id_separateur = a[3].index(':')
                self.liste_nomenclature.append([int(a[0]), int(a[1]), a[2], a[3][(id_separateur + 2):]])



















