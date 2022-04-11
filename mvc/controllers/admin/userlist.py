import web
import pyrebase
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/admin/")

class Userlist:
    def GET(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) #se crea un objeto para conectarse con firebase
            db = firebase.database()#se crea un objeto para usar el servicio de base de datos de firebase
            users = db.child("users").get()#se obtiene la informacion de la base de firebase
            return render.user_list(users)
        except Exception as error:
            print("Error UsersList.GET: {}".format(error))