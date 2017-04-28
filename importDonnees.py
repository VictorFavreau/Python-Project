import csv
import codecs
import sqlite3

class Installation :
    def __init__(self, nomInstall,numInstall,nomCommune,cp,nomLieuD,numVoie,nomVoie,longitude,latitude,accessH,nbPlacesP):
        self.nomInstall = nomInstall
        self.numInstall = numInstall
        self.nomCommune = nomCommune
        self.cp=cp
        self.nomLieuD = nomLieuD
        self.numVoie = numVoie
        self.nomVoie = nomVoie
        self.longitude = longitude
        self.latitude = latitude
        self.accessH = accessH
        self.nbPlacesP = nbPlacesP

    def display_installation(self):
        print("{0}, {1}, {2}".format(self.nomInstall, self.numInstall, self.nomCommune))

class Equipement :
    def __init__(self, numInstall, numEqu, nomEqu, nomBat, nbPTribune, accessH, dateMaj):
        self.numInstall = numInstall
        self.numEqu = numEqu
        self.nomEqu = nomEqu
        self.nomBat = nomBat
        self.nbPTribune = nbPTribune
        self.accessH = accessH
        self.dateMaj = dateMaj

    def display_equip(self):
        print("{0}, {1}, {2}".format(self.numInstall, self.numEqu, self.nomEqu))

class Activite :
    def __init__(self, numEqu, numAct, nomAct, typeAct):
        self.numEqu = numEqu
        self.numAct = numAct
        self.nomAct = nomAct
        self.typeAct = typeAct

    def display_act(self):
        print("{0}, {1}, {2}".format(self.numAct, self.nomAct, self.typeAct))

def importInstallation(nomFichier):
    # Ouverture de la connexion à la BD
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    # Préparation de la requete préparer
    insert_query = """INSERT INTO installations(nomInstall, numInstall, nomCommune, cdp, nomLieuDit, numVoie, nomVoie,
                        longitude, latitude, accessH, nbPlacesP) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    #Lit le fichier csv ligne par ligne
    fichier=csv.DictReader(codecs.open(nomFichier,"r","utf-8"))
    for row in fichier:
        #Pour chaque ligne on creer un nouvel objet installation
        install = Installation(row['Nom usuel de l\'installation'], row['Numéro de l\'installation'], row['Nom de la commune'], row['Code postal'], row['Nom du lieu dit'],\
            row['Numero de la voie'], row['Nom de la voie'], row['Longitude'], row['Latitude'], row['Accessibilité handicapés à mobilité réduite'],\
            row['Nombre total de place de parking'])
        # Insertion dans la BD de l'equipement
        c.execute(insert_query, (install.nomInstall, install.numInstall, install.nomCommune, install.cp, install.nomLieuD, install.numVoie, install.nomVoie,\
                                 install.longitude, install.latitude, install.accessH, install.nbPlacesP))
    conn.commit()
    conn.close()


def importEquipement(nomFichier):
    # Ouverture de la connexion à la BD
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    # Préparation de la requête préparer
    insert_query = """INSERT INTO equipements(InsNumeroInstall, EquipementId, EquNom, EquNomBatiment, 
                        EquNbPlaceTribune, EquAccesHandisAucun, EquDateMaj)
                        VALUES (?, ?, ?, ?, ?, ?, ?)"""
    # Lit le fichier csv ligne par ligne
    fichier = csv.DictReader(codecs.open(nomFichier, "r", "utf-8"))
    for row in fichier:
        # Pour chaque ligne on créer un nouvel objet équipement
        equip = Equipement(row['InsNumeroInstall'], row['EquipementId'], row['EquNom'], row['EquNomBatiment'], row['EquNbPlaceTribune'], \
            row['EquAccesHandisAucun'], row['EquDateMaj'])
        #Insertion dans la BD de l'équipement
        c.execute(insert_query, (equip.numInstall, equip.numEqu, equip.nomEqu, equip.nomBat, equip.nbPTribune, equip.accessH, equip.dateMaj))
    conn.commit()
    conn.close()

def importActivites(nomFichier):
    # Ouverture de la connexion à la BD
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    # Préparation de la requête préparer
    insert_query = """INSERT INTO activite(equipID, codeAct, nomAct, typeAct) VALUES (?, ?, ?, ?)"""
    # Lit le fichier csv ligne par ligne
    fichier = csv.DictReader(codecs.open(nomFichier, "r", "utf-8"))
    for row in fichier:
        # Pour chaque ligne on créer un nouvel objet activite
        act = Activite(row['EquipementId'], row['ActCode'], row['ActLib'], row['ActNivLib'])
        # Insertion dans la BD de l'équipement
        c.execute(insert_query, (act.numEqu, act.numAct, act.nomAct, act.typeAct))
    conn.commit()
    conn.close()

print("**** IMPORTATION DES INSTALLATIONS ****")
importInstallation("data/installations.csv")
print("**** IMPORTATION DES EQUIPEMENTS ****")
importEquipement("data/equipements.csv")
print("**** IMPORTATION DES ACTIVITEES ****")
importActivites("data/activites.csv")