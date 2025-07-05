from datetime import datetime

# isort: off
from fasthtml.common import *
from monsterui.all import *
# isort: on

from src.app_config import APP_NOMBRE
from src.auth.login import is_user_logged
# from src.data.DAO_users import UserDAO
from src.utils.general import debug_pause, debug_print

def login_form(next_url):
    return Title(APP_NOMBRE), Container(
            DivCentered(cls="min-h-screen flex items-center justify-center bg-muted")(
                Card(
                    DivVStacked(
                        DivLAligned(
                            UkIcon('recycle',height=30,width=30),
                            H2(APP_NOMBRE, cls="ml-2"),
                            cls="text-default"
                        ),
                        DividerSplit(cls="w-4/5 self-center border border-primary"),
                        DivVStacked(
                            H3("Iniciar sesión"),
                            UkIcon('log-in',height=30,width=30, cls="text-green-600"),
                        ),
                        Subtitle("Introduce tus credenciales para acceder al sistema"),
                        Form(
                            LabelInput("Nombre de usuario", id="username", placeholder="Tu nombre de usuario", autofocus=True),
                            LabelInput("Contraseña", id="password", type="password", placeholder="Tu contraseña"),   # ••••••••
                            Button("Acceder", cls=(ButtonT.primary, "w-full")),
                            cls="space-y-4", action="/login_post", method="POST"
                        ),
                        A("¿Olvidaste tu contraseña?", href="#", cls=(AT.muted, TextT.sm, "text-center"), uk_tooltip="title: Mala suerte, debes ser más cuidadoso...;pos: bottom")
                    ),
                    cls="w-full max-w-md p-6 space-y-6"
                ),
                Input(type="hidden", name="user_role", value="user"),  
                Input(type="hidden", name="next_url", value=next_url),
            )
        )


# Función para inicializar rutas de login
def init_routes(rt):

    @rt('/login_post')
    async def post(session, request):

        user_data = dict(await request.form())
        username = user_data.get("username", "")
        password = user_data.get("password", "")
        next_url = user_data.get("next_url", "/")
        user_data.get("user_role", "GENERAL")
        # debug_pause(username, password, user_data)
        # current_user = get_user_info(session) if is_user_logged(session) else None

        # Se supone que hemos comprobado si el username/password es correcto
        # Guardar el nuevo usuario loggeado
            # user_dao = UserDAO()
            # user = user_dao.get_user_by_username(username)
        # TODO: comprobar el password
            # autenticado = user.check_password(password=password.lower().strip()) if user else False
        autenticado = True
                
        if autenticado:
            # user.last_login = datetime.now()
            # user_dao.update(user)

            # session['user'] = {
            #     "username": user.username,
            #     "password": user.password,
            #     "role": user.role
            # }
            session['user'] = {
                "username": "admin",
                "password": "1234",
                "role": "admin"
            }

            # show_toast(mensaje="Acceso permitido.", tipo="success")
            add_toast(sess=session, message="Acceso permitido", typ="success")
            return RedirectResponse(next_url, status_code=303)
        
        # NO se ha autenticado
        # show_toast(mensaje="Usuario o contraseña incorrectos.", tipo="danger")
        add_toast(sess=session, message="Usuario o contraseña incorrectos.", typ="error")
        return RedirectResponse("/", status_code=303)

    @rt('/logout')
    def get(session):
        # Borrar el usuario y los forms de la session
        if session and is_user_logged(session):
            session.pop('user', None)
        if session and "form" in session:
            session.pop("form", None)
        if session and "form_principal" in session:
            session.pop("form_principal", None)


        # Volvemos al 'home'
        # show_toast(mensaje="Se ha cerrado la sesión.", tipo="info")
        add_toast(sess=session, message="Se ha cerrado la sesión.", typ="info")
        return RedirectResponse('/', status_code=303)
