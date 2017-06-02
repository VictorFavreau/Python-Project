import sqlite3

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
    c.execute(requete,(cdp))
    for row in c :
        ville.append(row[0])
    conn.close()
    print(ville)
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
    requete = """SELECT DISTINCT numInstall, nomInstall FROM installations WHERE nomCommune = ? ORDER BY nomInstall"""
    c.execute(requete,(nomCommune))
    for row in c:
        if row[1] != "":
            dico_install[row[0]] = row[1]
    conn.close()
    print(dico_install)
    return dico_install

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
    c.execute(requete,(numInstall))
    for row in c :
        codeEquip = row[0]
        # On récupère dans la table Installations tous les cdp et nom de villes dans la BD
        c1.execute(requete2,(codeEquip))
        for row1 in c1:
            dico_activites[row1[0]] = row1[1]
    conn.close()
    #print(dico_activites)
    return dico_activites

# Fonction qui récupère toutes les activités d'une ville
# Parametre nomCommune : Nom de la commune dont l'on souhaite connaître les activités
# Retourne un dico composé de toutes les activités de cette ville
def dico_activitesVille(nomCommune):
    dico_install = dico_installations(nomCommune)
    dico_activitesVille = {}
    for numInstall in dico_install:
        dico_activitesVille=dico_install.copy()
    print(dico_activitesVille)

# Fonction qui récupère toutes les installations possédant une activitée donnée d'une ville
# Parametre nomCommune : Nom de la commune dont l'on souhaite connaître les installations
#           nomActivitee : Nom de l'activitée dont l'on souhaite connaître les installations qui l'a propose
# Retourne un dico composé de toutes les installations d'une ville qui propose cette activitée
def dico_installActiv(nomCommune, nomActivitee):
    # Ouverture de la connexion à la BD
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    dico_installActiv = {}
    requete = """SELECT DISTINCT i.numInstall, i.nomInstall FROM equipements As e INNER JOIN activite As a ON e.EquipementId=a.equipID AND a.nomAct=? INNER JOIN installations As i ON e.InsNumeroInstall=i.numInstall AND i.nomCommune=?"""
    c.execute(requete,(nomActivitee, nomCommune))
    for row in c:
        dico_installActiv[row[0]] = row[1]
    print(dico_installActiv)
    conn.close()

dico_installActiv("Nantes","Tir à l'arc")