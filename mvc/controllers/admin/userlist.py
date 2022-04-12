import web
import pyrebase
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/admin/")

class Userlist:
    def GET(self):
        try:#Se intenta con este codigo
            print("Inicio_admin.GEt localId: ", web.cookies().get('localId'))#imprime la ID de la cookie
            if web.cookies().get('localId') == "None" : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina 
            elif web.cookies().get('localId') == None : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina 
            else:
                firebase = pyrebase.initialize_app(token.firebaseConfig) #se crea un objeto para conectarse con firebase
                db = firebase.database()#se crea un objeto para usar el servicio de base de datos de firebase
                users = db.child("users").get()
                return render.user_list(users)
        except Exception as error:
            print("Error Inicio.GET: {}".format(error)) #si exite un error, se imprime