import sqlite3
from bottle import get, post, request, run, template, route, static_file
from bottle import get, post, request, run
from dico_villes import *


@get('/index')
def get_index():
    return template('webpage/index')

@route('/search', method='GET')
def get_search():
    installation = dico_trouveInstall("Nantes","Handball / Mini hand / Handball de plage")
    return template('webpage/search', installation=installation)

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