import csv
import codecs
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
    fichier=csv.DictReader(codecs.open(nomFichier,"r","utf-8"))
    for row in fichier:
        install = Installation(row['Nom usuel de l\'installation'], row['Numéro de l\'installation'], row['Nom de la commune'], row['Code postal'], row['Nom du lieu dit'],\
            row['Numero de la voie'], row['Nom de la voie'], row['Longitude'], row['Latitude'], row['Accessibilité handicapés à mobilité réduite'], row['Nombre total de place de parking'])
        print(install.display_installation())

def importEquipement(nomFichier):
    fichier=csv.DictReader(codecs.open(nomFichier,"r","utf-8"))

    for row in fichier:
        equip = Equipement(row['InsNumeroInstall'], row['EquipementId'], row['EquNom'], row['EquNomBatiment'], row['EquNbPlaceTribune'], \
            row['EquAccesHandisAucun'], row['EquDateMaj'])
        print(equip.display_equip())

def importActivites(nomFichier):
    fichier=csv.DictReader(codecs.open(nomFichier,"r","utf-8"))
    for row in fichier:
        act = Activite(row['EquipementId'], row['ActCode'], row['ActLib'], row['ActNivLib'])
        print(act.display_act())

print("Création des objets installations\n")
importInstallation("data/installations.csv")
print("\n\nCréation des objets équipements\n")
importEquipement("data/equipements.csv")
print("\n\nCréation des objets activités\n")
importActivites("data/activites.csv")