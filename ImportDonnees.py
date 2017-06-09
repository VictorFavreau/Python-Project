import csv
import codecs
import sqlite3

class Installation :
    # Initialization of the "Installation" class
    def __init__(self, nomInstall, numInstall, nomCommune, cp, nomLieuD, numVoie, nomVoie, longitude, latitude, accessH, nbPlacesP):
        self.nomInstall = nomInstall
        self.numInstall = numInstall
        self.nomCommune = nomCommune
        self.cp         = cp
        self.nomLieuD   = nomLieuD
        self.numVoie    = numVoie
        self.nomVoie    = nomVoie
        self.longitude  = longitude
        self.latitude   = latitude
        self.accessH    = accessH
        self.nbPlacesP  = nbPlacesP

    # Displays the current "Installation" object
    def display_installation(self):
        print("{0}, {1}, {2}".format(self.nomInstall, self.numInstall, self.nomCommune))

class Equipement :
    # Initialization of the "Equipement" class
    def __init__(self, numInstall, numEqu, nomEqu, nomBat, nbPTribune, accessH, dateMaj, equX, equY):
        self.numInstall = numInstall
        self.numEqu = numEqu
        self.nomEqu = nomEqu
        self.nomBat = nomBat
        self.nbPTribune = nbPTribune
        self.accessH = accessH
        self.dateMaj = dateMaj
        self.equX = equX
        self.equY = equY

    # Displays the current "Equipement" object
    def display_equip(self):
        print("{0}, {1}, {2}".format(self.numInstall, self.numEqu, self.nomEqu))

class Activite :
    # Initialization of the "Activite" class
    def __init__(self, numEqu, numAct, nomAct, typeAct):
        self.numEqu = numEqu
        self.numAct = numAct
        self.nomAct = nomAct
        self.typeAct = typeAct

    # Displays the current "Activite" object
    def display_act(self):
        print("{0}, {1}, {2}".format(self.numAct, self.nomAct, self.typeAct))

def importInstallation(nomFichier):
    # Openning the Database connection
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()


    # Preparation of the prepared request
    insert_query = """INSERT INTO installations(nomInstall, numInstall, nomCommune, cdp, nomLieuDit, numVoie, nomVoie,
                        longitude, latitude, accessH, nbPlacesP) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    #Read CSV file line by line
    fichier=csv.DictReader(codecs.open(nomFichier,"r","utf-8"))

    for row in fichier:
        #For each row, a new Installation object is created
        install = Installation(row['Nom usuel de l\'installation'], row['Numéro de l\'installation'], row['Nom de la commune'], row['Code postal'], row['Nom du lieu dit'],\
            row['Numero de la voie'], row['Nom de la voie'], row['Longitude'], row['Latitude'], row['Accessibilité handicapés à mobilité réduite'],\
            row['Nombre total de place de parking'])
        # insert the installation into the database
        c.execute(insert_query, (install.nomInstall, install.numInstall, install.nomCommune, install.cp, install.nomLieuD, install.numVoie, install.nomVoie,\
                                 install.longitude, install.latitude, install.accessH, install.nbPlacesP))
    conn.commit()
    conn.close()



def importEquipement(nomFichier):
    # Openning the database connection
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    # Preparation of the prepared request
    insert_query = """INSERT INTO equipements(InsNumeroInstall, EquipementId, EquNom, EquNomBatiment, 
                            EquNbPlaceTribune, EquAccesHandisAucun, EquDateMaj, EquX, EquY)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    # Read CSV file line by line
    fichier = csv.DictReader(codecs.open(nomFichier, "r", "utf-8"))
    for row in fichier:
        # For each row, a new Equipement object is created
        equip = Equipement(row['InsNumeroInstall'], row['EquipementId'], row['EquNom'], row['EquNomBatiment'],
                           row['EquNbPlaceTribune'], \
                           row['EquAccesHandisAucun'], row['EquDateMaj'], row['EquGpsX'], row['EquGpsY'])
        #insert the Equipement into the database
        c.execute(insert_query, (equip.numInstall, equip.numEqu, equip.nomEqu, equip.nomBat, equip.nbPTribune, equip.accessH, equip.dateMaj, equip.equX, equip.equY))
    conn.commit()
    conn.close()

def importActivites(nomFichier):
    # Openning the database connection
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    # Preparation of the prepared request
    insert_query = """INSERT INTO activite(equipID, codeAct, nomAct, typeAct) VALUES (?, ?, ?, ?)"""
    # Read CSV file line by line
    fichier = csv.DictReader(codecs.open(nomFichier, "r", "utf-8"))
    for row in fichier:
        # For each row, a new Activity object is created
        act = Activite(row['EquipementId'], row['ActCode'], row['ActLib'], row['ActNivLib'])
        # insert the Activity into the database
        c.execute(insert_query, (act.numEqu, act.numAct, act.nomAct, act.typeAct))
    conn.commit()
    conn.close()

print("**** IMPORTATION OF INSTALLATIONS ****")
importInstallation("data/installations.csv")
print("**** IMPORTATION OF EQUIPEMENTS ****")
importEquipement("data/equipements.csv")
print("**** IMPORTATION OF ACTIVITEES ****")
importActivites("data/activites.csv")