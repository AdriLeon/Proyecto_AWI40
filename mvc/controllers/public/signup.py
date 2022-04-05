import web
import pyrebase
import firebase_config as token 
import app as app

render = web.template.render("mvc/views/public/")

class Signup:
    def GET(self):
        return render.signup()
    def POST(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth()
            db = firebase.database()
            formulario = web.input()
            name = formulario.name
            phone = formulario.phone
            email = formulario.email
            password = formulario.password
            user= auth.create_user_with_email_and_password(email, password)# nos permitira crear nuevo usuario y contraseña
            print(user['localId']) 
            data = {# se crea una variable, en ella introducirmos los valores del formulario en formato json (un diccionario)
                "name": name,
                "phone": phone,
                "email": email
            }
            results = db.child("users").child(user['localId']).set(data)#aqui almacenaremos los datos en la pase de datos, user para el nombre de la tabla, de ahi generamos otra rama que sera la de la localId
            web.setcookie('localId', user['localId'], 3600)
            print("localId: ", web.cookies().get('localId'))
            return web.seeother("login") # redirecciona a la pagina de login
        except Exception as error:
            format = json.loads(error.args[1])
            error = format['error']
            message = error['message']
            print("Error Login.POST: {}".format(message))
            web.setcookie('localId', '', 3600)
            return render.login(message)
