# isort: off
from fasthtml.common import *
from monsterui.all import *
# isort: on

import uuid

from datetime import datetime
from src.auth.login import is_user_admin, is_user_logged
from src.auth.login_routes import login_form

from src.app_config import APP_NOMBRE, NAVBAR_BG_COLOR, NAVBAR_FIXED_ON_TOP
from src.views.components.buttons import ConfirmRedirectLink
# from src.utils.js_scripts import show_toast


# Activar ToolTips
bootstrap_tooltips_js = Script(
    code="""
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
    """
)

# ------------------------------------------------------------------------ #
# Modal form
def myModal():
    return \
    Div(id='exampleModal', tabindex='-1', aria_labelledby='exampleModalLabel', aria_hidden='true', cls='modal fade')(
        Div(cls='modal-dialog')(
            Div(cls='modal-content')(
                Div(cls='modal-header')(
                    H1('Modal title', id='exampleModalLabel', cls='modal-title fs-5'),
                    Button(type='button', data_bs_dismiss='modal', aria_label='Close', cls='btn-close')
                ),
                Div(cls='modal-body')(
                    Card(
                        Form(
                            Div(cls='form-floating mb-3')(
                                Input(type='email', id='floatingInput', placeholder='name@example.com', cls='form-control'),
                                    Label('Email address', fr='floatingInput')
                                ),

                                Div(cls='form-floating')(
                                    Input(type='password', id='floatingPassword', placeholder='Password', cls='form-control'),
                                    Label('Password', fr='floatingPassword')
                                ),
                        )
                    )
                ),
                Div(cls='modal-footer')(
                    Button('Cerrar', type='button', data_bs_dismiss='modal', cls='btn btn-secondary'),
                    Button('Guardar cambios', type='button', data_bs_dismiss='modal', cls='btn btn-primary',
                           hx_get="/pag3", hx_target="#main-content")
                )
            )
        )
    )
# ------------------------------------------------------------------------ #

# Menú de opciones
def menu(session):
    # Si no se ha hecho login, presentamos la web para visitantes
    if not is_user_logged(session):
        ret = Ul(cls='navbar-nav me-auto ml-4 mb-2 mb-md-0')(
            Li(cls='nav-item')(
                A('Servicios', href='/servicios', cls='nav-link text-primary', hx_get='/servicios', hx_target='#main-content'),
            ),
            Li(cls='nav-item')(
                A('Noticias', href='/noticias', cls='nav-link text-primary', hx_get='/noticias', hx_target='#main-content')
            ),
            Li(cls='nav-item')(
                A('Contacto', href='/contactos', cls='nav-link text-primary', hx_get='/contacto', hx_target='#main-content')
            ),
        )

    else:  # Tenemos login, ahora tratar el 'user-role'
        ret =  Ul(cls='navbar-nav me-auto ml-4 mb-2 mb-md-0')(
            
            Li(cls="nav-item dropdown")(  # Ficheros
                A(data_bs_toggle="dropdown",
                  aria_expanded="false",
                  cls="nav-link dropdown-toggle text-primary")(
                    I(cls="bi-archive-fill text-primary px-1"), "Ficheros"),
                    Div(cls='dropdown-menu', style=f'background-color: {NAVBAR_BG_COLOR};')(
                        
                        A(I(cls="bi-person-circle text-primary px-1"),'Usuarios', cls='dropdown-item text-primary', hx_get='/usuarios', hx_target='#main-content') if is_user_admin(session) else "",
                        
                        Div(cls='dropdown-divider'),

                        A(I(cls="bi-diagram-2-fill text-primary px-1"),'Familias de artículos', cls='dropdown-item text-primary', hx_get='/familias', hx_target='#main-content'),

                        A(I(cls="bi-box-seam text-primary px-1"),'Artículos', hx_get='/articulos', hx_target='#main-content', cls='dropdown-item text-primary'),

                        Div(cls='dropdown-divider'),

                        A('Admin', href='/admin', cls='dropdown-item text-primary'),

                    ),
            ),
            
            Li(cls='nav-item px-1')( # Clientes
                A(cls='nav-link text-primary icon-link icon-link-hover',
                    hx_get='/clientes', hx_target='#main-content',
                    data_bs_toggle='tooltip',
                    title='Gestión de Clientes.', data_bs_placement='bottom')(
                        I(cls="bi-person-lines-fill text-primary"),
                        'Clientes',
                    ),
            ),
            
            Li(cls='nav-item px-1')( # Obras
                A(cls='nav-link text-primary icon-link icon-link-hover',
                    hx_get='/obras', hx_target='#main-content',
                    data_bs_toggle='tooltip',
                    title='Gestión de Obras', data_bs_placement='bottom')(
                        I(cls="bi-house-gear-fill text-primary"),
                        'Obras',
                    ),
            ),
            
            Li(cls='nav-item px-1')( # Partes
                A(cls='nav-link text-primary icon-link icon-link-hover',
                    hx_get='/partes', hx_target='#main-content',
                    data_bs_toggle='tooltip',
                    title='Gestión de Partes', data_bs_placement='bottom')(
                        I(cls="bi-file-earmark-ppt-fill text-primary"),
                        'Partes',
                    ),
            ),

            Li(cls='nav-item px-1')( # Contratos
                A(cls='nav-link text-primary icon-link icon-link-hover',
                    hx_get='/contratos', hx_target='#main-content',
                    data_bs_toggle='tooltip',
                    title='Gestión de Contratos', data_bs_placement='bottom')(
                        I(cls="bi-file-earmark-text-fill text-primary"),
                        'Contratos',
                    ),
            ),

            Li(cls='nav-item')( # Ventas
                A('Ventas',
                    href='#',
                    cls='nav-link text-primary',
                    hx_get='/ventas',
                    hx_target='#main-content',
                    data_bs_toggle='tooltip',
                    title='Gestión de Ventas', data_bs_placement='bottom',
                )
            ),

            Li(cls='nav-item dropdown')( # Reports
                A(data_bs_toggle='dropdown', aria_expanded='false', cls='nav-link dropdown-toggle text-primary')('Reports'),
                Div(cls='dropdown-menu', style=f'background-color: {NAVBAR_BG_COLOR};')(
                    A('Login', href='/login', cls='dropdown-item text-primary'),
                    A('Action 2', href='#', cls='dropdown-item text-primary', hx_get='/pag2', hx_target='#main-content'),
                    A('Forzar Logout', href='/logout', cls='dropdown-item text-primary'),
                    Div(cls='dropdown-divider'),
                    A('Admin', href='/admin', cls='dropdown-item text-primary'),
                ),
            ),

        )

    return ret

# Zona de Login
def zona_login(session):
    if is_user_logged(session):
        # Tenemos Login, presentamos opción de Logout
        session['user']['username']
        session['user']['role']
        ret = ConfirmRedirectLink(
            url="/logout",
            mensaje="Va a abandonar la sesión y para volver a acceder tendrá que introducir sus credenciales.",
            titulo="¿Quiere cerrar la sesión?",
            tipo_alerta="question",
            cls="btn btn-danger d-flex align-items-center gap-1 p-1",
            tooltip="Cerrar la sesión",
            children=[
                I(cls="bi-person-x fs-4"),
                Span(style="font-size: 0.9rem;")("admin"),
            ]
        )

    else:
        # No tenemos Login
        ret = A(cls='nav-link icon-link icon-link-hover pr-2',
            href="/login",
            hx_get='/login', hx_target='#main-content',
            data_bs_toggle='tooltip',
            title='Acceso Usuarios', data_bs_placement='bottom')(
                Button(cls="btn btn-success p-1 m-0")(
                    I(cls="bi-person-check fs-4 mx-1"),
                    Span("Acceso"),
                ),
        )
    
    return ret

# Navbar
def navbar(title, session):
    return Header(
    Nav(id="main-navbar", cls="fixed-top" if NAVBAR_FIXED_ON_TOP else "")(
        Div(cls='container-fluid')(
            
            # Logotipo
            A(cls='navbar-brand', href='/')(
                # Img(src='/static/img/icon.png', alt='Logo', cls='mr-1', height=48, width=48),
                I(cls="bi bi-recycle fs-1 fs-bold text-primary"),
            ),

            # Nombre de la app
            A(title, href='/', cls='navbar-brand ml-0 mr-4 text-primary fs-2 fw-bold'),
    

            # Botón Hamburger
            Button(
                type='button',
                data_bs_toggle='collapse', data_bs_target='#my-navbar',
                aria_controls='my-navbar', aria_expanded='false', aria_label='Cambar navegación',
                cls='navbar-toggler')(
                Span(cls='navbar-toggler-icon')
            ),

            Div(id='my-navbar', cls='collapse navbar-collapse w-full')(
                
                # Menú de opciones
                menu(session),
                
                # Zona de Login
                zona_login(session),
                
                # Fin zona de Login

                # Form(role='search')(
                #     Input(type='search', placeholder='Search', aria_label='Search', cls='form-control')
                # )
            ),
        )
    )
)

# main-content -> contenido
def contenido():
    # Main Content
    return  \
    Div(cls='col-sm-8 py-5 mx-auto')(
        H1('Piscinas Pepe'),
        P(cls='fs-5')(
            'Expertos en diseño, construcción y mantenimiento de piscinas',
        ),
        P("Somos una empresa familiar, fundada por nuestro padre José Sánchez Buendia (Pepe Piscinas) en 1.981"),
        P("A día de hoy, la gerencia de la empresa es responsabilidad de sus hijos José María y David Sánchez González. Nuestro padre (Pepe) es considerado toda una institución en el sector de la piscina en la Isla de Ibiza, y por eso es para nosotros un orgullo y a la vez una gran responsabilidad estar a cargo de la misma."),

        P(
            # Abrir el MODAL
            Button('Contáctanos', type='button', data_bs_toggle='modal', data_bs_target='#exampleModal', cls='btn btn-primary'),
        ),
    )

# main-content
def main_content():
    # Main Content
    return \
    Div(
        id='main-content',
        cls='p-2 rounded',
        style='background-color: gainsboro;'+'margin-top: 80px;' if NAVBAR_FIXED_ON_TOP else ''
        )(
        contenido()
    )

# Footer
def footer():
    # Footer
    return Footer(cls="p-1", style=f"position:fixed; left: 0; bottom: 0; width: 100%; text-align: center; background-color: {NAVBAR_BG_COLOR};")(
        Div(cls="d-flex justify-content-around")(
            Span(cls="text-secondary mt-3")(f"© {datetime.now().year} {APP_NOMBRE}. Todos los derechos reservados."),
            Button(
                cls="btn btn-danger p-1 m-2",
                onclick=f"scrollToId('under-navbar')")(
                    I(cls="bi-arrow-up-square"), title="Subir al principio.",
            )
        )
    )


def ex_navbar():
    return NavBar(
        A(Input(placeholder='search', autofocus=True)), 
        A(UkIcon("home")), 
        A('Page1',href='/rt1'), 
        A("Page2", href='/rt3'),
        brand=DivLAligned(
            UkIcon('home',height=30,width=30),
            H2("Título")
        ),
        cls="bg-gray-200 lg:p4 p-2 lg:pr-60"
    )

def logout_button(caption:str=""):
    return ConfirmRedirectLink(
        url="/logout",
        mensaje="Va a abandonar la sesión y para volver a acceder tendrá que introducir sus credenciales.",
        titulo="¿Quiere cerrar la sesión?",
        tipo_alerta="question",
        cls="btn bg-red-600 hover:bg-red-400 text-white lg:mr-2 border-0",
        tooltip="Cerrar la sesión",
        placement="right",
        children=[
            UkIcon('log-out',height=20,width=20),
            Span(style="font-size: 0.9rem;")(caption),
        ]
    )

def main_page(session:dict={}):
    # ----------------------------------------------------------------------------
    # 1. Sidebar
    sidebar = Div(
        cls="w-64 h-screen fixed inset-y-0 left-0 bg-gray-700 text-white overflow-auto hidden lg:block z-20 shadow-lg",
        id="sidebar"
    )(
        Div(cls="flex flex-col h-full")(
            Div(cls="flex-1")(
                # Logo
                Div(cls="hidden lg:flex items-center justify-center py-6")(
                    DivFullySpaced(
                        A(
                            DivLAligned(
                                UkIcon('recycle', height=30, width=30),
                                H3(APP_NOMBRE, cls="pl-2"),
                                cls="px-4"
                            ),
                            href='/', onclick="hideSidebar()"
                        ),
                        logout_button()
                    ),
                ),
                # Inicio
                DivHStacked(
                    UkIcon(icon="home", cls="ml-4"),
                    A("Inicio", href="/home", cls=(TextT.bold, "ml-1"), onclick="hideSidebar()")
                ),
                # Accordion de ventas y compras
                Accordion(
                    AccordionItem(
                        DivHStacked(UkIcon(icon="shopping-bag", cls="ml-4"), Span("Ventas", cls="ml-2")),
                        Ul(
                            Li(A('Presupuestos', hx_get='/servicios', hx_target="#main-content", onclick="hideSidebar()", cls="block")),
                            Li(A('Pedidos', href='/home', onclick="hideSidebar()", cls="block")),
                            hidden='',
                            id='uk-nav-ventas',
                            role='region',
                            aria_labelledby='uk-nav-label-ventas',
                            cls='uk-nav-sub uk-nav-primary !mt-0 !mb-0 !pb-0'
                        ),
                        cls="p-0 m-0 border-none"
                    ),
                    AccordionItem(
                        DivHStacked(UkIcon(icon="shopping-cart", cls="ml-4"), Span("Compras", cls="ml-2")),
                        Ul(
                            Li(A('Noticias', hx_get='/noticias', hx_target="#main-content", onclick="hideSidebar()", cls="block")),
                            Li(A('Servicios', hx_get='/servicios', hx_target="#main-content", onclick="hideSidebar()", cls="block")),
                            hidden='',
                            id='uk-nav-compras',
                            role='region',
                            aria_labelledby='uk-nav-label-compras',
                            cls='uk-nav-sub uk-nav-primary !mt-0 !mb-0 !pb-0'
                        ),
                        cls="border-none"
                    ),
                    multiple=False,
                    animation=True,
                    cls="!space-y-0 !m-0 !p-0"
                )
            ),
            # Botón fijo al fondo
            Div(cls="hidden lg:block p-4 mt-auto")(
                Button("Ver planes", cls=(ButtonT.primary, "w-full"))
            )
        )
    )

    sidebar = Div(
            cls="w-64 h-screen fixed inset-y-0 left-0 bg-gray-700 text-white overflow-auto hidden lg:block z-20 shadow-lg",
            id="sidebar"
        )(
            Div(cls="flex flex-col h-full")(
                Div(cls="flex-1")(
                    # Logo
                    Div(cls="hidden lg:flex items-center justify-center py-6")(
                        DivFullySpaced(
                            A(
                                DivLAligned(
                                    UkIcon('recycle', height=30, width=30),
                                    H3(APP_NOMBRE, cls="pl-2"),
                                    cls="px-4"
                                ),
                                href='/', onclick="hideSidebar()"
                            ),
                            logout_button()
                        )
                    ),
                    # Inicio
                    DivHStacked(
                        UkIcon(icon="home", cls="ml-4"),
                        A("Inicio", href="/home", cls=(TextT.bold, "ml-1"), onclick="hideSidebar()"),
                        cls="mt-0 mb-0 bg-red-200"  # Espaciado superior coherente
                    ),
                    # Accordion de ventas y compras
                    Accordion(
                        AccordionItem(
                            DivHStacked(UkIcon(icon="shopping-bag", cls="ml-4"), Span("Ventas", cls="ml-2")),
                            Ul(
                                Li(A('Presupuestos',
                                    hx_get='/servicios',
                                    hx_target="#main-content",
                                    onclick="hideSidebar()",
                                    cls="block px-4 py-[2px] hover:bg-secondary")),
                                Li(A('Pedidos',
                                    href='/home',
                                    onclick="hideSidebar()",
                                    cls="block px-4 py-[2px] hover:bg-secondary")),
                                hidden='',
                                id='uk-nav-ventas',
                                role='region',
                                aria_labelledby='uk-nav-label-ventas',
                                cls='uk-nav-sub uk-nav-primary !mt-0 !mb-0 !pb-0 !space-y-0'
                            ),
                            cls="mt-4"
                        ),
                        AccordionItem(
                            DivHStacked(UkIcon(icon="shopping-cart", cls="ml-4"), Span("Compras", cls="ml-2")),
                            Ul(
                                Li(A('Noticias',
                                    hx_get='/noticias',
                                    hx_target="#main-content",
                                    onclick="hideSidebar()",
                                    cls="block px-4 py-[2px] hover:bg-secondary")),
                                Li(A('Servicios',
                                    hx_get='/servicios',
                                    hx_target="#main-content",
                                    onclick="hideSidebar()",
                                    cls="block px-4 py-[2px] hover:bg-secondary")),
                                hidden='',
                                id='uk-nav-compras',
                                role='region',
                                aria_labelledby='uk-nav-label-compras',
                                cls='uk-nav-sub uk-nav-primary !mt-0 !mb-0 !pb-0 !space-y-0'
                            ),
                            cls="mt-4"
                        ),
                        multiple=False,
                        animation=True,
                        cls="!space-y-0 !m-0 !p-0 !border-none !border-0 bg-red-200",
                        style="padding: 0px; margin: 0px;"
                    )
                ),
                # Botón fijo al fondo
                Div(cls="hidden lg:block p-4 mt-auto")(
                    Button("Ver planes", cls=(ButtonT.primary, "w-full"))
                )
            )
        )

    sidebar = Div(
        cls="w-64 h-screen fixed inset-y-0 left-0 bg-gray-700 text-white overflow-auto hidden lg:block z-20 shadow-lg",
        id="sidebar"
    )(
        Div(cls="flex flex-col h-full")(
            Div(cls="flex-1")(
                # Logo
                Div(cls="hidden lg:flex items-center justify-center py-6")(
                    DivFullySpaced(
                        A(
                            DivLAligned(
                                UkIcon('recycle', height=30, width=30),
                                H3(APP_NOMBRE, cls="pl-2"),
                                cls="px-4"
                            ),
                            href='/', onclick="hideSidebar()"
                        ),
                        logout_button()
                    )
                ),

                # Contenedor de Inicio + Accordion (espaciado controlado)
                Div(cls="flex flex-col gap-0 !space-y-0")(
                    # Inicio
                    DivHStacked(
                        UkIcon(icon="home", cls="ml-4"),
                        A("Inicio", href="/home", cls=(TextT.bold, "ml-5"), onclick="hideSidebar()"),
                        cls="mt-0 mb-0"
                    ),

                    # Línea separadora
                    Div(cls="h-[14px]"),
                    Hr(cls="mt-4"),

                    # Accordion de secciones
                    Accordion(
                        AccordionItem(
                            DivHStacked(UkIcon(icon="shopping-bag", cls="ml-4"), Span("Ventas", cls="ml-2")),
                            Ul(
                                Li(A('Presupuestos',
                                    hx_get='/servicios',
                                    hx_target="#main-content",
                                    onclick="hideSidebar()",
                                    cls="block px-4 py-[2px] hover:bg-secondary")),
                                Li(A('Pedidos',
                                    href='/home',
                                    onclick="hideSidebar()",
                                    cls="block px-4 py-[2px] hover:bg-secondary")),
                                hidden='',
                                id='uk-nav-ventas',
                                role='region',
                                aria_labelledby='uk-nav-label-ventas',
                                cls='uk-nav-sub uk-nav-primary !mt-0 !mb-0 !pb-0 !space-y-0'
                            ),
                            cls="mt-0 mb-0"
                        ),
                        AccordionItem(
                            DivHStacked(UkIcon(icon="shopping-cart", cls="ml-4"), Span("Compras", cls="ml-2")),
                            Ul(
                                Li(A('Noticias',
                                    hx_get='/noticias',
                                    hx_target="#main-content",
                                    onclick="hideSidebar()",
                                    cls="block px-4 py-[2px] hover:bg-secondary")),
                                Li(A('Servicios',
                                    hx_get='/servicios',
                                    hx_target="#main-content",
                                    onclick="hideSidebar()",
                                    cls="block px-4 py-[2px] hover:bg-secondary")),
                                hidden='',
                                id='uk-nav-compras',
                                role='region',
                                aria_labelledby='uk-nav-label-compras',
                                cls='uk-nav-sub uk-nav-primary !mt-0 !mb-0 !pb-0 !space-y-0'
                            ),
                            cls="mt-0 mb-0"
                        ),
                        multiple=False,
                        animation=True,
                        cls="!space-y-0 !m-0 !p-0"
                    )
                )
            ),

            # Botón fijo al fondo
            Div(cls="hidden lg:block p-4 mt-auto")(
                Button("Ver planes", cls=(ButtonT.primary, "w-full"))
            )
        )
    )



    # ----------------------------------------------------------------------------
    # 2. Navbar móvil (solo en <lg): "Mi Empresa" clicable y botón menú
    #    - añadimos 'shadow-md' para sombra debajo
    mobile_navbar = Div(
        cls="flex items-center justify-between p-4 bg-gray-700 text-white lg:hidden shadow-md"
        )(
            DivFullySpaced(
                DivLAligned(
                    A(
                        DivLAligned(
                            UkIcon('recycle',height=30,width=30),
                            H3(APP_NOMBRE, cls="pl-2"),
                            cls="lg:px-4 px-2"
                        ),
                        href='/home', onclick="hideSidebar()"
                    ),
                ),
                DivRAligned(logout_button(), cls="pr-6"),
            ),
            Label(
                "☰",
                cls="btn btn-primary",
                onclick="toggleSidebar()"
            )
       )

    # ----------------------------------------------------------------------------
    # 3. Contenido principal ajustado para pantalla móvil
    #    - pt-4 en móvil para quedar cerca del navbar
    #    - lg:pt-0 en desktop
    #    - ml-0 lg:ml-64 para dejar espacio al sidebar en desktop
    contenido_home = Div(cls="h-screen pt-1 lg:pt-0 ml-0 lg:ml-64", id="main-content")(
        Div(cls="h-full bg-red-200 flex items-center justify-center px-4 py-8")(
            Container(  # Aquí solo centramos el Card sin afectar el fondo
                Card(
                    DivVStacked(
                        DivLAligned(
                            UkIcon('recycle', height=30, width=30),
                            H2(APP_NOMBRE, cls="ml-2"),
                            cls="text-default"
                        ),
                        DividerSplit(cls="w-4/5 self-center border border-primary"),
                        H5(f"Hola, {session['user']['username'].capitalize()}"),
                        Subtitle("Bienvenido a tu aplicación de gestión favorita !"),
                        DivHStacked(cls="pt-8")(
                            logout_button(caption=session['user']['username']),
                        ),
                    ),
                    cls="w-full max-w-md p-2 space-y-2"
                ),
                # footer(),
            )
        )
    )

    # ----------------------------------------------------------------------------
    # 4. JavaScript para alternar la visibilidad del sidebar en móvil
    js_toggle = """
    function toggleSidebar() {
      var s = document.getElementById('sidebar');
      if (s.classList.contains('hidden')) {
        s.classList.remove('hidden');
      } else {
        s.classList.add('hidden');
      }
    }
    function hideSidebar() {
      var s = document.getElementById('sidebar');
      s.classList.add('hidden');
    }
    """

    # ----------------------------------------------------------------------------
    # 5. Montaje final: sidebar, navbar móvil, contenido y <script>
    layout = Div()(
        sidebar,
        mobile_navbar,
        contenido_home,
        Script(js_toggle)
    )

    return Title(APP_NOMBRE), layout


# Home-Page
def home_page(session, request, contenido: str = ""):
    # Comprobar si tenemos login
    if not is_user_logged(session):
        # No hay login, mostrar el form de login
        return login_form(next_url='/')
        
    else:
        # Tenemos Login
        return main_page(session)

# Servicios
def servicios_page(session, request):
    return DivVStacked(
        H1("Servicios"),
        P(cls="mt-4")("Este es el párrafo 1 de Servicios."),
        Button(cls=ButtonT.primary)("Hola click")
    )

# Noticias
def noticias_page(session, request):
    ct2 = Div(cls='col-sm-8 py-5 mx-auto')(
        H1('NOTICIAS' + f": User: {session['user_id'] if 'user_id' in session else 'No ha login'}", cls='display-5 fw-normal'),
        P(cls='fs-5')(
            'This example shows how responsive offcanvas menus work within the navbar. For positioning of navbars, checkout the',
            A('top', href='/docs/5.3/examples/navbar-static/'),
            'and',
            A('fixed top', href='/docs/5.3/examples/navbar-fixed/'),
            'examples.'
        ),
        P("From the top down, you'll see a dark navbar, light navbar and a responsive navbar—each with offcanvases built in. Resize your browser window to the large breakpoint to see the toggle for the offcanvas."),
        P(
            A('Learn more about offcanvas navbars »', href='/docs/5.3/components/navbar/#offcanvas', role='button', cls='btn btn-primary')
        )
    )
    return ct2

# Contacto 
def contacto_page(session, request):
    ct3 = Div(cls='col-sm-8 py-5 mx-auto')(
        H1('CONTACTO', cls='display-5 fw-normal'),
        P(cls='fs-5')(
            'This example shows how responsive offcanvas menus work within the navbar. For positioning of navbars, checkout the',
            A('top', href='/docs/5.3/examples/navbar-static/'),
            'and',
            A('fixed top', href='/docs/5.3/examples/navbar-fixed/'),
            'examples.'
        ),
        P("From the top down, you'll see a dark navbar, light navbar and a responsive navbar—each with offcanvases built in. Resize your browser window to the large breakpoint to see the toggle for the offcanvas."),
        P(
            A('Learn more about offcanvas navbars »', href='/docs/5.3/components/navbar/#offcanvas', role='button', cls='btn btn-primary')
        )
    )

    return ct3