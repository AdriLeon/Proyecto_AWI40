import web
import pyrebase
import firebase_config as token 
import app as app

render = web.template.render("mvc/views/admin/")

class Userupdate:
    def GET(self, localId):#se invoca al entrar a la ruta /user_update
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) #se crea un objeto para conectarse con firebase
            db = firebase.database()#se crea un objeto para usar el servicio de base de datos de firebase
            user = db.child("users").child(localId).get()#se obtiene la informacion de la base de firebase
            return render.user_update(user)
        except Exception as error:
            print("Error user update.GET: {}".format(error))
    def POST(self, localId):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) #se crea un objeto para conectarse con firebase
            db = firebase.database()
            formulario = web.input()
            phone = formulario.phone
            nivel = formulario.nivel
            status = formulario.status
            data = {
                "phone": phone,
                "nivel": nivel,
                "status": status
            }
            db.child("users").child(localId).update(data)
            return web.seeother("/user_list") 
        except Exception as error:
            print("Error user update.GET: {}".format(error))