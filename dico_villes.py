import sqlite3
import json


"""
       Function retrieving all cities associated with a zip code.

        :return: returns a list of city
"""
def city_dictionary(zip):
    """
            Opening the database connection.
    """
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()

    """
                Creation dictionary of the cities with as key the postal code and as value the name of the city.
    """
    city = []

    request = """SELECT DISTINCT nomCommune FROM installations WHERE cdp = ? ORDER BY cdp, nomCommune"""
    c.execute(request,(zip,))
    for row in c :
        city.append(row[0])
    conn.close()

    return city


"""
        Function that returns a list of Installations based on a city name in a JSON format.

        :return: Installation dictionary (JSON format)
"""
def installation_dictionary(nomCommune):
    """
        Opening the database connection.
    """
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()

    """
        Creation dictionary of Installations with as key the Installation number and as value the Installation name.
    """
    dico_install = {}

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
    """
        Converting the list to JSON format.
    """
    json_data = json.dumps(liste_install)
    return json_data

"""
        Function that returns all activities associated with an Installation.

        :return: Activity dictionary
"""
def activity_dictionary(install_id):
    """
            Opening the database connection.
    """
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()
    c1 = conn.cursor()
    """
            Creation dictionary of Activity with as key the Activity number and as value the Activity name.
    """
    activity_dictionary = {}

    first_request   = """SELECT EquipementId FROM equipements WHERE InsNumeroInstall =?"""
    second_request  = """SELECT DISTINCT codeAct, nomAct FROM activite WHERE equipID =? ORDER BY nomAct"""
    c.execute(first_request,(install_id,))
    for row in c :
        equipment_code = row[0]

        c1.execute(second_request,(equipment_code,))
        for row1 in c1:
            activity_dictionary[row1[0]] = row1[1]

    conn.close()
    return activity_dictionary

"""
        Function that returns all the activities of a city.

        :return: returns nothing
"""
def city_activities_dictionary(city_name):
    """
                Opening the database connection.
    """
    conn = sqlite3.connect("python_project.db")
    city_activity_dic = {}
    c = conn.cursor()
    request = """SELECT DISTINCT a.codeAct, a.nomAct FROM activite As a INNER JOIN equipements As e ON a.equipID=e.EquipementID INNER JOIN installations As i ON e.InsNumeroInstall=i.numInstall AND i.nomCommune=?"""
    c.execute(request, (city_name,))
    for row in c:
        city_activity_dic[row[0]] = row[1]

    conn.close()
    return city_activity_dic


"""
        Function returning all installations of a given city according to the activity chosen.

        :return: returns an Activity dictionary in JSON format
"""
def installations_activity_list(city_name, activity_name):
    """
                Opening the database connection.
    """
    conn = sqlite3.connect("python_project.db")
    c = conn.cursor()

    request = """SELECT DISTINCT i.numInstall, i.nomInstall, i.nomCommune, i.cdp, i.nomLieuDit, i.numVoie, i.nomVoie,
                    i.accessH, i.nbPlacesP, e.EquX, e.EquY, i.longitude, i.latitude FROM equipements As e INNER JOIN activite As a ON e.EquipementId=a.equipID 
                    AND a.nomAct=? INNER JOIN installations As i ON e.InsNumeroInstall=i.numInstall AND i.nomCommune=?"""
    c.execute(request,(activity_name, city_name))
    i=0
    liste_install = []
    for row in c:
        installation_activity_dic = {}
        installation_activity_dic["numInstall"] = row[0]
        installation_activity_dic["nomInstall"] = row[1]
        installation_activity_dic["nomCommune"] = row[2]
        installation_activity_dic["cdp"] = row[3]
        installation_activity_dic["nomLieuDit"] = row[4]
        installation_activity_dic["numVoie"] = row[5]
        installation_activity_dic["nomVoie"] = row[6]
        installation_activity_dic["accessH"] = row[7]
        installation_activity_dic["nbPlacesP"] = row[8]
        installation_activity_dic["longitude"] = row[9]
        installation_activity_dic["latitude"] = row[10]
        liste_install.insert(i,installation_activity_dic)
        i=i+1
    conn.close()
    """
            Converting the list to JSON format.
    """
    json_data = json.dumps(liste_install)
    return json_data