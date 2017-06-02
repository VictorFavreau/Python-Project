import sqlite3

from bottle import get, post, request, run

#Création du dictionnaire liant code postal et villes
@get('/cdp')
def creerDict_cdp():


run(host='localhost', port=8080)