import csv
import codecs
class Installation :
    def __init__(self, nomInstall,numInstall,nomCommune,codeINSEE,cp,nomLieuD,numVoie,nomVoie,location,longitude,latitude,accessH,nbPlacesP):
        self.nomInstall = nomInstall
        self.numInstall = numInstall
        self.nomCommune = nomCommune
        self.codeINSEE = codeINSEE
        self.cp=cp
        self.nomLieuD = nomLieuD
        self.numVoie = numVoie
        self.nomVoie = nomVoie
        self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.accessH = accessH
        self.nbPlacesP = nbPlacesP

    def display_personne(self):
        print("{0}, {1}, {2}, {3}".format(self.nomInstall, self.numInstall, self.nomCommune, self.location))

class Equipement :
    def __int__(self,codeINSEE,nomCommune,equipID,codeAct,nomAct,typeAct):
        self.codeINSEE = codeINSEE
        self.nomCommune = nomCommune
        self.equipID = equipID
        self.codeAct = codeAct
        self.nomAct = nomAct
        self.typeAct = typeAct

def importEquipement(nomFichier):
    fichier=csv.reader(codecs.open(nomFichier,"r","utf-8"))
    for row in fichier:
        #install = Installation(row[1])
        print(row[0])

importEquipement("installations_table.csv")