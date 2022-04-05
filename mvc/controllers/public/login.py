import web
import pyrebase
import firebase_config as token 
import app as app

render = web.template.render("mvc/views/public/")

class Login: 
    def GET(self):
        try: 
            message = None # se crear una variable para el mensaje de error
            return render.login(message) # renderiza la pagina login.html con el mensaje
        except Exception as error: 
            message = "Error en el sistema" # se almamacena nuestro mensaje de error
            print("Error Login.GET: {}".format(error)) # se imprime el error que ocurrio
            return render.login(message) # se renderiza nuevamente alogin con el mensaje de error

    def POST(self):
        try:
            message = None #se crea una variable para nuestro mensaje de error
            firebase = pyrebase.initialize_app(token.firebaseConfig)
            auth = firebase.auth() # Este nos permitira autenticar con firebase
            formulario = web.input() #tomara los datos del formulario
            email = formulario.email #el email del formulario se almacena en la variable
            password = formulario.password #el password del formulario se almacena en la variable
            print(email,password)#imprimimos el correo y la contraseña para verificar que este tomando los datos
            user = auth.sign_in_with_email_and_password(email, password) # este método devolverá los datos del usuario, incluido un token que puede usar para cumplir con las reglas de seguridad.
            print(user['localId']) #Si los datos son correctos se mostrara la ID del usuario
            web.setcookie('localId', user['localId'], 3600) #creamos la cookie donde se almacena nuestra ID
            print("localId: ", web.cookies().get('localId'))#iprimimos nuestra cookies para verificar que se haya creado
            return web.seeother("inicio") # redirecciona a la pagina de inicio
        except Exception as error:
            format = json.loads(error.args[1]) #presenta el error en formato JSON
            error = format['error'] #Obtenemos el JSON del nuestro error
            message = error['message'] #obtenemos el mensaje
            print("Error Login.POST: {}".format(message))#imprimimos el mensaje 
            web.setcookie('localId', '', 3600)#se elimina la ID de nuestra cookie
            return render.login(message)#renderizamos la pagina, pero mostrando esta vez el mensaje
