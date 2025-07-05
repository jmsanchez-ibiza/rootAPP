# main.py

from dotenv import find_dotenv, load_dotenv
from fasthtml.common import *
from monsterui.all import *

from src.app_config import APP_NOMBRE
# Cargar variables de entorno
# Busca el archivo .env
env_file = find_dotenv(".env")

if env_file and os.path.exists(env_file):
    # Carga el archivo .env si existe
    load_dotenv(env_file, override=True)
    print(f"Archivo de configuración ({env_file}) cargado exitosamente.")
else:
    # Imprime un mensaje de error y termina el programa si el archivo no se encuentra
    print("ERROR: No se encontró el fichero de configuración: .env")
    sys.exit(1)

# Leer variables de entorno
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
PORT = int(os.getenv("PORT", 8000))
LIVE = os.getenv("LIVE", "False").lower() == "true"

# Configurar headers
hdrs = [
    Script(src='https://cdn.jsdelivr.net/npm/sweetalert2@11'),
    Theme.green.headers(daisy=True),
    Link(rel="icon", type="image/x-ico", href="img/recycle.png"),
    Link(rel='stylesheet', href='css/styles.css', type='text/css'),
    Script(src="js/main.js"),
]

# Creamos la aplicación con tema "blue" de MonsterUI + DaisyUI activo
app, rt = fast_app(
    live=LIVE,
    debug=DEBUG,
    port=PORT,
    static_path="static",
    hdrs=hdrs,
    htmlkw={"lang":"es", "data-theme":"light"}, # Pasamos estos parámetros al <html>
)

# 📌 Configurar Toasts -> TENGO QUE VER COMO FUNCIONA ESTO
setup_toasts(app, duration=1500)


# Importar los controladores
from src.auth import login_routes
from src.auth.login import login_required, user_role_required
from src.controllers import (
    home_controller,
)

# Iniciar las routes
login_routes.init_routes(rt)
home_controller.init_routes(rt)






# Ejecutar la app
if __name__ == "__main__":
    print("EJECUTANDO CON: " + "serve()->Live" if LIVE else "Uvicorn")

    if LIVE:
        print("Serve")
        serve()
    else:
        port = int(os.getenv("PORT", default=5001))
        print(f"Uvicorn {port=} {LIVE=}")

        uvicorn.run(
            'main:app',
            host='0.0.0.0',
            port=port,
            workers=4,
            reload=False
        )






# def ex_navbar():
#     return NavBar(
#         A(Input(placeholder='search')), 
#         A(UkIcon("home")), 
#         A('Page1',href='/rt1'), 
#         A("Page2", href='/rt3'),
#         brand=DivLAligned(
#             UkIcon('home',height=30,width=30),
#             H2("Título")
#         ),
#         cls="bg-gray-200 lg:p4 p-2 lg:pr-60"
#     )


# @rt
# def index():
#     # ----------------------------------------------------------------------------
#     # 1. Sidebar con sombra en el lateral derecho e inferior
#     sidebar = Div(
#         # cls="w-64 h-screen fixed inset-y-0 left-0 bg-base-200 text-base-content overflow-auto hidden lg:block z-20 shadow-lg",
#         cls="w-64 h-screen fixed inset-y-0 left-0 bg-gray-700 text-white overflow-auto hidden lg:block z-20 shadow-lg",
#         id="sidebar"
#     )(
#         # Logo / título de la empresa (solo visible en desktop)
#         Div(cls="hidden lg:flex items-center justify-center py-6")(
#             A(
#                 DivLAligned(
#                     UkIcon('recycle',height=30,width=30),
#                     H3(APP_NOMBRE, cls="pl-2"),
#                     cls="px-4"
#                 ),
#                 hx_get='/', hx_target="#main-content", onclick="hideSidebar()"
#             ), cls=(TextT.lg, TextT.bold, "pb-6 pt-6")
#         ),
#         # "Inicio" carga el contenido de home vía HTMX
#         DivHStacked(
#             UkIcon(icon="home", cls="ml-4"),
#             A(
#                 "Inicio",
#                 href="/home",
#                 cls=(TextT.bold, "ml-1"),
#                 hx_get="/home",
#                 hx_target="#main-content",
#                 onclick="hideSidebar()"
#             ),
#         ),
        
#         Accordion(
#             AccordionItem(
#                 DivHStacked(
#                     UkIcon(icon="chart-bar", cls="ml-4"),
#                     Span("Ventas", cls="ml-2")
#                 ),
#                 Ul(
#                     Li(
#                         A('Presupuestos', hx_get='/mi-zona', hx_target="#main-content", onclick="hideSidebar()", style="padding: 3px" )
#                     ),
#                     Li(
#                         A('Pedidos', hx_get='/home', hx_target="#main-contecnt", onclick="hideSidebar()", style="padding: 3px" )
#                     ),
#                     hidden='',
#                     id='uk-nav-ventas',
#                     role='region',
#                     aria_labelledby='uk-nav-label-ventas',
#                     cls='uk-nav-sub uk-nav-primary !mt-0 !mb-0 !pb-0'
#                 ),
#                 cls="p-0 m-0 border-none"
#             ),
#             AccordionItem(
#                 DivHStacked(
#                     UkIcon(icon="chart-bar", cls="ml-4"),
#                     Span("Compras", cls="ml-2")
#                 ),
#                 Ul(
#                     Li(
#                         A('Facturas de compra', hx_get='/mi-zona', hx_target="#main-content", onclick="hideSidebar()", style="padding: 3px;")
#                     ),
#                     Li(
#                         A('Pedidos de compra', hx_get='/home', hx_target="#main-content", onclick="hideSidebar()", style="padding: 3px;")
#                     ),
#                     hidden='',
#                     id='uk-nav-compras',
#                     role='region',
#                     aria_labelledby='uk-nav-label-compras',
#                     cls='uk-nav-sub uk-nav-primary !mt-0 !mb-0 !pb-0'
#                 ),
#                 cls="border-none"
#             ),
#             multiple=False,
#             animation=True,
#             cls="space-y-0 !m-0 !p-0"  # clave para quitar separación entre ítems
#         ),

#         # Botón "Ver planes" al final (solo en desktop)
#         Div(cls="hidden lg:block mt-3")(
#                 Button("Ver planes", cls=(ButtonT.primary, "w-full"))
#         )
#     )

#     # ----------------------------------------------------------------------------
#     # 2. Navbar móvil (solo en <lg): "Mi Empresa" clicable y botón menú
#     #    - añadimos 'shadow-md' para sombra debajo
#     mobile_navbar = Div(
#         cls="flex items-center justify-between p-4 bg-gray-700 text-white lg:hidden shadow-md"
#         )(
#         A(
#             DivLAligned(
#                 UkIcon('recycle',height=30,width=30),
#                 H3(APP_NOMBRE, cls="pl-2"),
#                 cls="lg:px-4 px-2"
#             ),
#             hx_get='/', hx_target="#main-content", onclick="hideSidebar()"
#         ),
#         Label(
#             "☰",
#             cls="btn btn-primary",
#             onclick="toggleSidebar()"
#         )
#     )

#     # ----------------------------------------------------------------------------
#     # 3. Contenido principal ajustado para pantalla móvil
#     #    - pt-4 en móvil para quedar cerca del navbar
#     #    - lg:pt-0 en desktop
#     #    - ml-0 lg:ml-64 para dejar espacio al sidebar en desktop
#     contenido_principal = Div(cls="pt-1 lg:pt-0 ml-0 lg:ml-64", id="main-content")(
#         ex_navbar(),
#         H1("Bienvenido al Dashboard", cls=(TextT.xl, TextT.bold, "mb-6")),
#         P("Esta es la zona principal de la aplicación de gestión empresarial.", cls=TextPresets.muted_sm)
#     )

#     # ----------------------------------------------------------------------------
#     # 4. JavaScript para alternar la visibilidad del sidebar en móvil
#     js_toggle = """
#     function toggleSidebar() {
#       var s = document.getElementById('sidebar');
#       if (s.classList.contains('hidden')) {
#         s.classList.remove('hidden');
#       } else {
#         s.classList.add('hidden');
#       }
#     }
#     function hideSidebar() {
#       var s = document.getElementById('sidebar');
#       s.classList.add('hidden');
#     }
#     """

#     # ----------------------------------------------------------------------------
#     # 5. Montaje final: sidebar, navbar móvil, contenido y <script>
#     layout = Div()(
#         sidebar,
#         mobile_navbar,
#         contenido_principal,
#         Script(js_toggle)
#     )

#     return Title(APP_NOMBRE), layout

