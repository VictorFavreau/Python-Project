import sqlite3

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
          EquDateMaj date)"""
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
c.execute("DROP TABLE IF EXISTS equipements_activite")
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
