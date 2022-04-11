import web
import pyrebase
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/operador/")


class Dashboard_user:
    def GET(self):
        return render.dashboard_user()