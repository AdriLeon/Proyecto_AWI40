import web

urls = (
    '/', 'mvc.controllers.public.index.Index',
    '/login', 'mvc.controllers.public.login.Login',
    '/signup', 'mvc.controllers.public.signup.Signup',
    '/inicio_admin', 'mvc.controllers.admin.inicio_admin.Inicio_admin',
    '/inicio_user', 'mvc.controllers.operador.inicio_user.Inicio_user',
    '/logout', 'mvc.controllers.operador.logout.Logout',
    '/logout', 'mvc.controllers.admin.logout.Logout',
    '/user_list', 'mvc.controllers.admin.userlist.Userlist',
    '/user_update/(.*)', 'mvc.controllers.admin.userupdate.Userupdate',
    '/dashboard_admin', 'mvc.controllers.admin.dashboard_admin.Dashboard_admin',
    '/dashboard_user', 'mvc.controllers.operador.dashboard_user.Dashboard_user',
    '/register', 'mvc.controllers.admin.register.Register',
    '/recuperar', 'mvc.controllers.public.recuperar.Recuperar'
)


app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()