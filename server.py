from bottle import get, post, request, run


@post('/cdp')
def affiche_cdp():
    print("cdp")


run(host='localhost', port=8080)