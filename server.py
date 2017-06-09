import sqlite3
from bottle import get, post, request, run, template, route, static_file
from bottle import get, post, request, run
from dico_villes import *



@route('/')
def get_index():
    return template('webpage/index')


@route('/index')
def get_index():
    return template('webpage/index')



@route('/city', method='POST')
def get_city():
    lv_cdp = request.forms.get('zip')

    liste_ville = dico_villes(lv_cdp)

    if(len(liste_ville) != 0):
        return template('webpage/city', zip=lv_cdp, liste_ville=liste_ville)
    else:
        return template('webpage/index')


@route('/activity', method='POST')
def get_activity():

    lv_cdp = request.forms.get('zip')
    lv_ccommune = request.forms.get('select_ville')
    print(lv_ccommune)


    liste_activite = dico_activitesVille(lv_ccommune)

    return template('webpage/activity', zip=lv_cdp, commune=lv_ccommune, liste_activites=liste_activite)

@route('/search', method='POST')
def get_search():

    lv_commune = request.forms.get('ville')
    lc_activite = request.forms.get('select_activite')




    if(lc_activite == "Toutes"):
        liste_install = dico_installations(lv_commune)
    else:
        liste_install = dico_installActiv(lv_commune, lc_activite)


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