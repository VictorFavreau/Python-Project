import sqlite3
from bottle import get, post, request, run, template, route, static_file
from bottle import get, post, request, run
from dico_villes import *



@route('/index')
def get_index():
    return template('webpage/index')

@route('/city/<zip>')
def get_city(zip):
    global lv_cdp
    lv_cdp = zip

    liste_ville = dico_villes(zip)
    return template('webpage/city', zip=lv_cdp, liste_ville=liste_ville)

@route('/activity/<select_ville>')
def get_activity(select_ville):

    recup_string = select_ville.split("_")
    liste_activite = dico_activitesVille(recup_string[1])

    return template('webpage/activity', zip=recup_string[0], commune=recup_string[1], liste_activites=liste_activite)

@route('/search/<select_activity>')
def get_search(select_activity):

    recup_string = select_activity.split("_")

    if(recup_string[1] == "Toutes"):
        liste_install = dico_installations(recup_string[0])
    else:
        liste_install = dico_installActiv(recup_string[0], recup_string[1])


    print(liste_install)

    return template('webpage/search', liste_install=liste_install)

@route("/webpage/css/<filename>")
def style(filename):
    return static_file(filename, root='webpage/css')

@route("/webpage/img/<filename>")
def images(filename):
    return static_file(filename, root='webpage/img')

@route("/webpage/img/base/<filename>")
def images_base(filename):
    return static_file(filename, root='webpage/img/base')

@route("/webpage/js/<filename>")
def javascript(filename):
    return static_file(filename, root='webpage/js')

@route("/webpage/plugins/owl-carousel/<filename>")
def plugin_owl(filename):
    return static_file(filename, root='webpage/plugins/owl-carousel')

@route("/webpage/plugins/rs-plugin/css/<filename>")
def plugin_rs_css(filename):
    return static_file(filename, root='webpage/plugins/rs-plugin/css')

@route("/webpage/plugins/rs-plugin/js/<filename>")
def plugin_rs_css(filename):
    return static_file(filename, root='webpage/plugins/rs-plugin/js')

@route("/webpage/plugins/rs-plugin/assets/<filename>")
def plugin_rs_assets(filename):
    return static_file(filename, root='webpage/plugins/rs-plugin/assets')

@route("/webpage/css/fonts/<filename>")
def fonts(filename):
    return static_file(filename, root='webpage/css/fonts')

@route("/webpage/css/font/<filename>")
def font(filename):
    return static_file(filename, root='webpage/css/font')


run(host='localhost', port=8080)