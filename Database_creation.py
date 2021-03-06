import os
import sqlite3
from ImportDonnees import *

# open the database connection
conn = sqlite3.connect("python_project.db")
c = conn.cursor()

# Creation of the "equipements" table
c.execute("DROP TABLE IF EXISTS equipements")
lvc_equipment_request = """CREATE TABLE equipements (id integer PRIMARY KEY,
          InsNumeroInstall integer,
          EquipementId integer,
          EquNom text,
          EquNomBatiment text,
          EquNbPlaceTribune integer,
          EquAccesHandisAucun integer,
          EquDateMaj date,
          EquX real,
          EquY real)"""
c.execute(lvc_equipment_request)


# Creation of the "activite" table
c.execute("DROP TABLE IF EXISTS activite")
lvc_activity_request = """CREATE TABLE activite (id integer PRIMARY KEY,
          equipID integer,
          codeAct integer,
          nomAct text,
          typeAct text)"""
c.execute(lvc_activity_request)


# Creation of the "equipements_activite" table
c.execute("DROP TABLE IF EXISTS installations")
lvc_installation_bd = """CREATE TABLE installations (id integer PRIMARY KEY,
          nomInstall text,
          numInstall integer,
          nomCommune text,
          cdp integer,
          nomLieuDit text,
          numVoie integer,
          nomVoie text,
          longitude real,
          latitude real,
          accessH integer,
          nbPlacesP integer)"""
c.execute(lvc_installation_bd)

conn.commit()

print("**** IMPORTATION OF INSTALLATIONS ****")
importInstallation("data/installations.csv")
print("**** IMPORTATION OF EQUIPEMENTS ****")
importEquipement("data/equipements.csv")
print("**** IMPORTATION OF ACTIVITEES ****")
importActivites("data/activites.csv")
