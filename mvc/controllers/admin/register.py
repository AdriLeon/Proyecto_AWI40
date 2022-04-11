import web
import pyrebase
import firebase_config as token 
import app as app
import json

render = web.template.render("mvc/views/admin/")

class Register:
    def GET(self):
        return render.register()
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