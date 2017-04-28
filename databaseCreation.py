import sqlite3

# ouvre la connexion à la base de données

conn = sqlite3.connect("python_project.db")
c = conn.cursor()

# creation de la table equipements
c.execute("DROP TABLE IF EXISTS equipements")
requete_equipements = """CREATE TABLE equipements (id integer PRIMARY KEY,
          InsNumeroInstall text,
          EquipementId text,
          EquNom text,
          EquNomBatiment text,
          EquNbPlaceTribune text,
          EquAccesHandisAucun text,
          EquGpsX text,
          EquGpsY text,
          EquDateMaj text)"""
c.execute(requete_equipements)

# creation de la table activite
c.execute("DROP TABLE IF EXISTS activite")
requete_activite = """CREATE TABLE activite (id integer PRIMARY KEY,
          equipID text,
          codeAct text,
          nomAct text,
          typeAct text)"""
c.execute(requete_activite)

# creation de la table installation_table
c.execute("DROP TABLE IF EXISTS equipements_activite")
requete_installation_table = """CREATE TABLE equipements_activite (id integer PRIMARY KEY,
          nomInstall text,
          numInstall text,
          nomCommune text,
          cdp text,
          nomLieuDit text,
          numVoie text,
          nomVoie text,
          longitude text,
          latitude text,
          accessH text,
          nbPlacesP text)"""
c.execute(requete_installation_table)


conn.commit()

print("Tables 'equipements', 'activite' et 'equipements_activite' crées avec succès !")
# insert une entrée

#insert_query = "INSERT INTO t_table(code, label) VALUES (?, ?)"
#c.execute(insert_query, (1, "test"))

#conn.commit()

#SELECT sur la table

#c.execute("SELECT code, label FROM t_table")

#for row in c:
#   print(row)

#conn.close()  # ferme la connexion à la base de données