import web
import pyrebase
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/admin/")

class Register:
    def GET(self):
        try:#Se intenta con este codigo
            print("Inicio_admin.GEt localId: ", web.cookies().get('localId'))#imprime la ID de la cookie
            if web.cookies().get('localId') == "None" : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina de login
            elif web.cookies().get('localId') == None : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina de login
            else:
                return render.register()
        except Exception as error:
            print("Error Inicio.GET: {}".format(error))

    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth()
            db = firebase.database()
            formulario = web.input()
            name = formulario.name
            phone = formulario.phone
            email = formulario.email
            password = '      '
            nivel = formulario.nivel
            status = formulario.status
            user= auth.create_user_with_email_and_password(email, password)# nos permitira crear nuevo usuario y contraseña
            print(user['localId'])
            data = {# se crea una variable, en ella introducirmos los valores del formulario en formato json (un diccionario)
                "name": name,
                "phone": phone,
                "email": email,
                "nivel": nivel,
                "status": status
            }
            results = db.child("users").child(user['localId']).set(data)
            return web.seeother("/register") 
        except Exception as error:
            format = json.loads(error.args[1])
            error = format['error']
            message = error['message']
            print("Error Login.POST: {}".format(message))
            return render.register(message)