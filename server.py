import sqlite3
from bottle import get, post, request, run, template, route, static_file
from bottle import get, post, request, run
from dico_villes import *


"""
    Redirection des liens de navigation.
"""
@route('/')
def get_index():
    return template('webpage/index')


@route('/index')
def get_index():
    return template('webpage/index')


@route('/city', method='POST')
def get_city():
    lv_cdp   = request.forms.get('zip')
    city_dic = city_dictionary(lv_cdp)

    if(len(city_dic) != 0):
        return template('webpage/city', zip=lv_cdp, liste_ville=city_dic)
    else:
        return template('webpage/index')


@route('/activity', method='POST')
def get_activity():

    zip_code = request.forms.get('zip')
    city     = request.forms.get('select_ville')
    city     = city.encode('ISO-8859-15').decode()

    activity_list = city_activities_dictionary(city)

    return template('webpage/activity', zip=zip_code, commune=city, liste_activites=activity_list)


@route('/search', method='POST')
def get_search():

    city     = request.forms.get('ville')
    city     = city.encode('ISO-8859-15').decode()
    activity = request.forms.get('select_activite')

    if(activity == "Toutes"):
        installation_list = installation_dictionary(city)
    else:
        installation_list = installations_activity_list(city, activity)

    print("liste: " + installation_list)


    return template('webpage/search', liste_install=installation_list)



"""
    Redirecting template links.
"""

@route("/webpage/css/<filename>")
def style(filename):
    return static_file(filename, root='webpage/css')

@route("/webpage/img/<filename>")
def pict(filename):
    return static_file(filename, root='webpage/img')

@route("/webpage/img/base/<filename>")
def pict_base(filename):
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