import web
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/operador/")

class Logout:
    def GET(self):
        web.setcookie('localId', None, 3600)#eliminara los datos de la ID
        print("Logout.GEt localId: ", web.cookies().get('localId'))#imprime la ID de la cookie
        return web.seeother('/login')#nos renderiza a la pagina de login

