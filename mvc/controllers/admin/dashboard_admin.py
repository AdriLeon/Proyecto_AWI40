import web
import pyrebase
import firebase_config as token 
import app as app
import json
import random

render = web.template.render("mvc/views/admin/")


class Dashboard_user:
    def GET(self):
        try:#Se intenta con este codigo
            print("Inicio_admin.GEt localId: ", web.cookies().get('localId'))#imprime la ID de la cookie
            if web.cookies().get('localId') == "None" : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina de login
            elif web.cookies().get('localId') == None : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina de login
            else:
                return render.dashboard_admin()
        except Exception as error:
            print("Error Inicio.GET: {}".format(error)) #si exite un error, se imprime
        
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
        return web.seeother("/dashboard_admin")