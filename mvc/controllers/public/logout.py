import web
import firebase_config as token 
import app as app

render = web.template.render("mvc/views/public/")
class Logout:
    def GET(self):
        web.setcookie('localId', '', 3600)#eliminara los datos de la ID
        return web.seeother('/login')#nos renderiza a la pagina de login

