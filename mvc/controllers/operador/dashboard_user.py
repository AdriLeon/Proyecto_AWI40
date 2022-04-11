import web
import pyrebase
import firebase_config as token 
import app as app
import json
import random

render = web.template.render("mvc/views/operador/")


class Dashboard_user:
    def GET(self):
        return render.dashboard_user()
    def POST(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        db = firebase.database()
        suc_hum1 =  random.randint(1, 40)
        suc_temp1 = random.randint(14, 32)
        suc_hum2 = random.randint(1, 40)
        suc_temp2= random.randint(14, 32)
        print(suc_hum1)
        print(suc_temp1)
        print(suc_hum2)
        print(suc_temp2)
        data_sucur1 = {
            "temperatura": suc_temp1,
            "humedad": suc_hum1,
        }
        data_sucur2 = {
            "temperatura": suc_temp2,
            "humedad": suc_hum2,
        }
        db.child("sucursales").child("sucursal_1").update(data_sucur1)
        db.child("sucursales").child("sucursal_2").update(data_sucur2)
        return web.seeother("/dashboard_user")