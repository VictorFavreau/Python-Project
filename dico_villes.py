import sqlite3
import json

# Fonction qui récupère toutes les villes disponible avec ce code postale
# Parametre cdp : Code postal choisit dont on souhaite les villes
# Retourne une liste composé de toutes les villes de ce code postale avec les villes de ce code postal

def dico_villes(cdp):
    #Ouverture de la connexion à la BD
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    #Création dictionnaire des villes avec comme clé le code postal et la valeur le nom de la ville
    ville = []
    #On récupère dans la table Installations tous les cdp et nom de villes dans la BD
    requete = """SELECT DISTINCT nomCommune FROM installations WHERE cdp = ? ORDER BY cdp, nomCommune"""
    c.execute(requete,(cdp,))
    for row in c :
        ville.append(row[0])
    conn.close()
    return ville

# Fonction qui récupère toutes les installations d'une ville
# Parametre nomCommune : Nom de la commune demandée
# Retourne un dico composé de toutes les installations dans cette ville avec le numéro et le nom d'installation
def dico_installations(nomCommune):
    # Ouverture de la connexion à la BD
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    # Création dictionnaire des villes avec comme clé le code postal et la valeur le nom de la ville
    dico_install = {}
    # On récupère dans la table Installations tous les cdp et nom de villes dans la BD
    requete = """SELECT DISTINCT i.numInstall, i.nomInstall, i.nomCommune, i.cdp, i.nomLieuDit, i.numVoie, i.nomVoie,
                    i.accessH, i.nbPlacesP, e.EquX, e.EquY, i.longitude, i.latitude FROM equipements As e 
                    INNER JOIN installations As i ON e.InsNumeroInstall=i.numInstall AND i.nomCommune=?"""
    c.execute(requete,(nomCommune,))
    i = 0
    liste_install = []
    for row in c:
        dico_install = {}
        dico_install["numInstall"] = row[0]
        dico_install["nomInstall"] = row[1]
        dico_install["nomCommune"] = row[2]
        dico_install["cdp"] = row[3]
        dico_install["nomLieuDit"] = row[4]
        dico_install["numVoie"] = row[5]
        dico_install["nomVoie"] = row[6]
        dico_install["accessH"] = row[7]
        dico_install["nbPlacesP"] = row[8]
        dico_install["longitude"] = row[9]
        dico_install["latitude"] = row[10]
        liste_install.insert(i, dico_install)
        i = i + 1
    conn.close()
    # Conversion en JSON
    json_data = json.dumps(liste_install)
    return json_data

# Fonction qui récupère toutes les activités d'une installation
# Parametre numInstall : Numéro de l'installation dont l'on souhaite connaître les activités
# Retourne un dico composé de toutes les activités de cette installation avec le code et le nom de l'activité
def dico_activites(numInstall):
    # Ouverture de la connexion à la BD
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    c1 = conn.cursor()
    # Création dictionnaire des villes avec comme clé le code postal et la valeur le nom de la ville
    dico_activites = {}
    #On récupère le numéro d'équipement pour récupérer les activités
    requete = """SELECT EquipementId FROM equipements WHERE InsNumeroInstall =?"""
    requete2 = """SELECT DISTINCT codeAct, nomAct FROM activite WHERE equipID =? ORDER BY nomAct"""
    c.execute(requete,(numInstall,))
    for row in c :
        codeEquip = row[0]
        # On récupère dans la table Installations tous les cdp et nom de villes dans la BD
        c1.execute(requete2,(codeEquip,))
        for row1 in c1:
            dico_activites[row1[0]] = row1[1]
    conn.close()
    return dico_activites

# Fonction qui récupère toutes les activités d'une ville
# Parametre nomCommune : Nom de la commune dont l'on souhaite connaître les activités
# Retourne un dico composé de toutes les activités de cette ville
def dico_activitesVille(nomCommune):
    conn = sqlite3.connect("python_project.db")
    dico_activitesVille = {}
    c = conn.cursor()
    requete = """SELECT DISTINCT a.codeAct, a.nomAct FROM activite As a INNER JOIN equipements As e ON a.equipID=e.EquipementID INNER JOIN installations As i ON e.InsNumeroInstall=i.numInstall AND i.nomCommune=?"""
    c.execute(requete, (nomCommune,))
    for row in c:
        dico_activitesVille[row[0]] = row[1]

    conn.close()
    return dico_activitesVille

# Fonction qui récupère toutes les installations possédant une activitée donnée d'une ville
# Parametre nomCommune : Nom de la commune dont l'on souhaite connaître les installations
#           nomActivitee : Nom de l'activitée dont l'on souhaite connaître les installations qui l'a propose
# Retourne un dico composé de toutes les installations d'une ville qui propose cette activitée
def dico_installActiv(nomCommune, nomActivitee):
    # Ouverture de la connexion à la BD
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()

    requete = """SELECT DISTINCT i.numInstall, i.nomInstall, i.nomCommune, i.cdp, i.nomLieuDit, i.numVoie, i.nomVoie,
                    i.accessH, i.nbPlacesP, e.EquX, e.EquY, i.longitude, i.latitude FROM equipements As e INNER JOIN activite As a ON e.EquipementId=a.equipID 
                    AND a.nomAct=? INNER JOIN installations As i ON e.InsNumeroInstall=i.numInstall AND i.nomCommune=?"""
    c.execute(requete,(nomActivitee, nomCommune))
    i=0
    liste_install = []
    for row in c:
        dico_installActiv = {}
        dico_installActiv["numInstall"] = row[0]
        dico_installActiv["nomInstall"] = row[1]
        dico_installActiv["nomCommune"] = row[2]
        dico_installActiv["cdp"] = row[3]
        dico_installActiv["nomLieuDit"] = row[4]
        dico_installActiv["numVoie"] = row[5]
        dico_installActiv["nomVoie"] = row[6]
        dico_installActiv["accessH"] = row[7]
        dico_installActiv["nbPlacesP"] = row[8]
        dico_installActiv["longitude"] = row[9]
        dico_installActiv["latitude"] = row[10]
        liste_install.insert(i,dico_installActiv)
        i=i+1
    conn.close()
    #Conversion en JSON
    json_data = json.dumps(liste_install)
    return json_data