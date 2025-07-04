from functools import wraps

from fasthtml.common import *
from starlette.requests import Request

from src.utils.general import debug_pause, debug_print
# from src.utils.js_scripts import show_toast


def _obtener_parametros(*args):
    # args, puede tener un <starlette.requests.Request> o un diccionario que 
    # sería la session
    user = None
    session = {}
    request = None
    if len(args) > 1:
        # args tiene 1 o 2 argumentos
        if isinstance(args[0], dict): session = args[0]
        if isinstance(args[1], dict): session = args[1]
        if isinstance(args[0], Request): request = args[0]
        if isinstance(args[1], Request): request = args[1]
        
    if session and "user" in session:
        user = session.get("user", None)
    return session, request, user

def login_required(func):
    """ Decorador para restringir acceso solo a usuarios autenticados """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Cargar parámetros recibidos
        # debug_pause(len(args), args)
        session, request, user = _obtener_parametros(*args)
        # debug_pause(session, request, user)
        if not user:
            # next_url = request.url.path  # Capturar la URL actual
            # redir_url = f"{login_redir}?{urlencode({'next': next_url})}"
            # show_toast(mensaje="Para poder acceder a esta página debe Iniciar la sessión.", tipo="error")
            add_toast(sess=session, message="Para poder acceder a esta página debe Iniciar la sessión.", typ="error")
            return RedirectResponse("/", status_code=303)

        request.scope['user'] = user  # Pasar el usuario a la request
        return func(*args, **kwargs)  # Llamar a la función original con sus argumentos originales
    return wrapper

def user_role_required(required_role: str = ""):
    """ Decorador para restringir acceso por roles """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Cargar parámetros recibidos
            session, request, user = _obtener_parametros(*args)
            
            if not user:
                # next_url = request.url.path  # Capturar la URL actual
                # redir_url = f"{login_redir}?{urlencode({'next': next_url})}"
                return RedirectResponse("/", status_code=303)

            # input(f"INPUT-PAUSE: user_role_required: {required_role} {user['role']=}")
            if 'role' in user and user['role'].lower().strip() != required_role.lower().strip():
                return Div(
                    # show_toast(
                    #     mensaje="NO tiene acceso a esta opción.",
                    #     hpos="center",
                    #     vpos="top",
                    #     tipo="danger",
                    #     segundos=3
                    #     ),
                    )
                # TODO: Dirigir a un modal que da el mensaje y vuelve a home

            request.scope['user'] = user  # Pasar el usuario a la request
            return func(*args, **kwargs)  # Llamar a la función original con sus argumentos originales
        return wrapper
    return decorator

# Comprobar si hemos hecho login, user_logged no está vacío
def is_user_logged(session):
    return True if isinstance(session, dict) and 'user' in session and session['user'] else False

# Obtener información del usuario loggeado
def get_user_info(session):
    ret_dict = session['user'] if 'user' in session else {}
    return ret_dict

# Comprobar si el user es 'ADMIN'
def is_user_admin(session):
    user_info = get_user_info(session)
    # debug_print(user_info, session)
    return False if not user_info else user_info['role'].lower() == "admin"
