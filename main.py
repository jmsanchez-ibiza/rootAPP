# main.py

from fasthtml.common import (
    Label as HtmlLabel,
    Div, H1, H2, H3, P, Ul, Li, A, Title, Script, serve
)
from monsterui.all import *  # Componentes estilizados de MonsterUI

# Creamos la aplicación con tema "blue" de MonsterUI + DaisyUI activo
app, rt = fast_app(hdrs=Theme.green.headers(daisy=True))


@rt
def index():
    # ----------------------------------------------------------------------------
    # 1. Sidebar con sombra en el lateral derecho e inferior
    sidebar_COPY = Div(
        cls="w-64 h-screen fixed inset-y-0 left-0 bg-base-200 text-base-content overflow-auto hidden lg:block z-20 shadow-lg",
        id="sidebar"
    )(
        # Logo / título de la empresa (solo visible en desktop)
        Div(cls="hidden lg:flex items-center justify-center py-6")(
            H1("Mi Empresa", cls=(TextT.lg, TextT.bold))
        ),
        # Lista de navegación
        Ul(cls="menu p-4 space-y-2")(
            # "Inicio" carga el contenido de home vía HTMX
            Li(
                A(
                    UkIcon(icon="home", cls="mr-2"),
                    "Inicio",
                    href="/home",
                    cls=TextT.normal,
                    hx_get="/home",
                    hx_target="#main-content",
                    onclick="hideSidebar()"
                )
            ),
            # "Mi Zona"
            Li(
                A(
                    UkIcon(icon="user", cls="mr-2"),
                    "Mi Zona",
                    href="/mi-zona",
                    cls=TextT.normal,
                    hx_get="/mi-zona",
                    hx_target="#main-content",
                    onclick="hideSidebar()"
                )
            ),
            Li(
                A(
                    UkIcon(icon="users", cls="mr-2"),
                    "Contactos",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),
            Li(
                A(
                    UkIcon(icon="chart-bar", cls="mr-2"),
                    "Ventas",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),
            Li(
                A(
                    UkIcon(icon="shopping-bag", cls="mr-2"),
                    "Compras",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),
            Li(
                A(
                    UkIcon(icon="briefcase", cls="mr-2"),
                    "CRM",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),
            Li(
                A(
                    UkIcon(icon="users", cls="mr-2"),
                    "RRHH",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),
            Li(
                A(
                    UkIcon(icon="clipboard-list", cls="mr-2"),
                    "Inventario",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),
            Li(
                A(
                    UkIcon(icon="folder-open", cls="mr-2"),
                    "Proyectos",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),
            Li(
                A(
                    UkIcon(icon="wallet", cls="mr-2"),
                    "Tesorería",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),
            Li(
                A(
                    UkIcon(icon="book-alt", cls="mr-2"),
                    "Contabilidad",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),
            # Botón "Ver planes" al final (solo en desktop)
            Div(cls="hidden lg:block mt-6")(
                Button("Ver planes", cls=(ButtonT.primary, "w-full"))
            )
        )
    )

    # Definición completa de `sidebar` con Accordion en “Ventas”
    sidebar_ACCORION = Div(
        cls="w-64 h-screen fixed inset-y-0 left-0 bg-base-200 text-base-content \
            overflow-auto hidden lg:block z-20 shadow-lg",
        id="sidebar"
    )(
        # Logo / título de la empresa (solo visible en desktop)
        Div(cls="hidden lg:flex items-center justify-center py-6")(
            H1("Mi Empresa", cls=(TextT.lg, TextT.bold))
        ),

        # Menú principal en modo acordeón
        Accordion(
            # Inicio
            AccordionItem(
                DivLAligned(UkIcon(icon="home", cls="mr-2"), P("Inicio", cls=TextT.normal)),
                A(
                    "",
                    href="/home",
                    hx_get="/home",
                    hx_target="#main-content",
                    cls="block w-full h-full",
                    onclick="hideSidebar()"
                )
            ),

            # Mi Zona
            AccordionItem(
                DivLAligned(UkIcon(icon="user", cls="mr-2"), P("Mi Zona", cls=TextT.normal)),
                A(
                    "",
                    href="/mi-zona",
                    hx_get="/mi-zona",
                    hx_target="#main-content",
                    cls="block w-full h-full",
                    onclick="hideSidebar()"
                )
            ),

            # Ventas (con subopciones)
            AccordionItem(
                DivLAligned(UkIcon(icon="chart-bar", cls="mr-2"), P("Ventas", cls=TextT.normal)),
                Ul(cls="menu p-2 pl-8 space-y-1")(
                    Li(
                        A(
                            "Facturas",
                            href="#",
                            cls=TextT.normal,
                            onclick="hideSidebar()"
                        )
                    ),
                    Li(
                        A(
                            "Presupuestos",
                            href="#",
                            cls=TextT.normal,
                            onclick="hideSidebar()"
                        )
                    ),
                    Li(
                        A(
                            "Pedidos",
                            href="#",
                            cls=TextT.normal,
                            onclick="hideSidebar()"
                        )
                    ),
                )
            ),

            # Compras
            AccordionItem(
                DivLAligned(UkIcon(icon="shopping-bag", cls="mr-2"), P("Compras", cls=TextT.normal)),
                A(
                    "",
                    href="#",
                    cls="block w-full h-full",
                    onclick="hideSidebar()"
                )
            ),

            # CRM
            AccordionItem(
                DivLAligned(UkIcon(icon="briefcase", cls="mr-2"), P("CRM", cls=TextT.normal)),
                A(
                    "",
                    href="#",
                    cls="block w-full h-full",
                    onclick="hideSidebar()"
                )
            ),

            # RRHH
            AccordionItem(
                DivLAligned(UkIcon(icon="users", cls="mr-2"), P("RRHH", cls=TextT.normal)),
                A(
                    "",
                    href="#",
                    cls="block w-full h-full",
                    onclick="hideSidebar()"
                )
            ),

            # Inventario
            AccordionItem(
                DivLAligned(UkIcon(icon="clipboard-list", cls="mr-2"), P("Inventario", cls=TextT.normal)),
                A(
                    "",
                    href="#",
                    cls="block w-full h-full",
                    onclick="hideSidebar()"
                )
            ),

            # Proyectos
            AccordionItem(
                DivLAligned(UkIcon(icon="folder-open", cls="mr-2"), P("Proyectos", cls=TextT.normal)),
                A(
                    "",
                    href="#",
                    cls="block w-full h-full",
                    onclick="hideSidebar()"
                )
            ),

            # Tesorería
            AccordionItem(
                DivLAligned(UkIcon(icon="wallet", cls="mr-2"), P("Tesorería", cls=TextT.normal)),
                A(
                    "",
                    href="#",
                    cls="block w-full h-full",
                    onclick="hideSidebar()"
                )
            ),

            # Contabilidad
            AccordionItem(
                DivLAligned(UkIcon(icon="book-alt", cls="mr-2"), P("Contabilidad", cls=TextT.normal)),
                A(
                    "",
                    href="#",
                    cls="block w-full h-full",
                    onclick="hideSidebar()"
                )
            ),

            # Botón “Ver planes” (solo en desktop)
            Div(cls="hidden lg:block mt-6")(
                Button("Ver planes", cls=(ButtonT.primary, "w-full"))
            )
        )
    )

    # Definición completa de `sidebar` con “Ventas” como collapse cerrado por defecto,
    # sin espacio extra entre secciones, y con líneas divisorias.

    sidebar = Div(
        cls="w-64 h-screen fixed inset-y-0 left-0 bg-base-200 text-base-content \
            overflow-auto hidden lg:block z-20 shadow-lg",
        id="sidebar"
    )(
        # Logo / título (solo en desktop), con sombra inferior
        Div(cls="hidden lg:flex items-center justify-center py-6 shadow-md")(
            H1("Mi Empresa", cls=(TextT.lg, TextT.bold))
        ),

        # Lista de navegación: sin padding/margin y con líneas entre items
        Ul(cls="menu p-0 m-0 divide-y divide-base-300")(
            # Inicio
            Li(cls="p-0")(
                A(
                    UkIcon(icon="home", cls="mr-2"),
                    "Inicio",
                    href="/home",
                    hx_get="/home",
                    hx_target="#main-content",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),

            # Mi Zona
            Li(cls="p-0")(
                A(
                    UkIcon(icon="user", cls="mr-2"),
                    "Mi Zona",
                    href="/mi-zona",
                    hx_get="/mi-zona",
                    hx_target="#main-content",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),

            # Ventas con collapse cerrado por defecto
            Li(cls="p-0")(
                Div(
                    cls="collapse collapse-arrow collapse-close bg-base-200 p-0",
                    tabindex="0"  # necesario para que funcione el toggle
                )(
                    # Título del collapse
                    Div(cls="collapse-title flex items-center pl-4")(
                        UkIcon(icon="chart-bar", cls="mr-2"),
                        P("Ventas", cls=TextT.normal)
                    ),
                    # Contenido oculto hasta abrir
                    Div(cls="collapse-content p-0")(
                        Ul(cls="menu p-0 m-0 space-y-1 ml-8")(
                            Li(cls="p-0")(
                                A(
                                    "Facturas",
                                    href="#",
                                    cls=TextT.normal,
                                    onclick="hideSidebar()"
                                )
                            ),
                            Li(cls="p-0")(
                                A(
                                    "Presupuestos",
                                    href="#",
                                    cls=TextT.normal,
                                    onclick="hideSidebar()"
                                )
                            ),
                            Li(cls="p-0")(
                                A(
                                    "Pedidos",
                                    href="#",
                                    cls=TextT.normal,
                                    onclick="hideSidebar()"
                                )
                            ),
                        )
                    )
                )
            ),

            # Compras
            Li(cls="p-0")(
                A(
                    UkIcon(icon="shopping-bag", cls="mr-2"),
                    "Compras",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),

            # CRM
            Li(cls="p-0")(
                A(
                    UkIcon(icon="briefcase", cls="mr-2"),
                    "CRM",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),

            # RRHH
            Li(cls="p-0")(
                A(
                    UkIcon(icon="users", cls="mr-2"),
                    "RRHH",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),

            # Inventario
            Li(cls="p-0")(
                A(
                    UkIcon(icon="clipboard-list", cls="mr-2"),
                    "Inventario",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),

            # Proyectos
            Li(cls="p-0")(
                A(
                    UkIcon(icon="folder-open", cls="mr-2"),
                    "Proyectos",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),

            # Tesorería
            Li(cls="p-0")(
                A(
                    UkIcon(icon="wallet", cls="mr-2"),
                    "Tesorería",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),

            # Contabilidad
            Li(cls="p-0")(
                A(
                    UkIcon(icon="book-alt", cls="mr-2"),
                    "Contabilidad",
                    href="#",
                    cls=TextT.normal,
                    onclick="hideSidebar()"
                )
            ),

            # Botón “Ver planes” (solo en desktop)
            Div(cls="hidden lg:block mt-6 p-4")(
                Button("Ver planes", cls=(ButtonT.primary, "w-full"))
            )
        )
    )

    sidebar = Div(
        Ul(
            Li(
                A(
                    Div('Getting Started', cls='flex justify-between items-center w-full'),
                    href='#',
                    id='uk-nav-9',
                    role='button',
                    aria_controls='uk-nav-10',
                    aria_expanded='false',
                    aria_disabled='false'
                ),
                Ul(
                    Li(
                        A('Getting Started', href='#', hx_get='/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Tutorial App', href='#', hx_get='/tutorial_app', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    id='uk-nav-10',
                    role='region',
                    aria_labelledby='uk-nav-9',
                    hidden='',
                    cls='uk-nav-sub uk-nav-primary'
                ),
                cls='uk-parent'
            ),
            Li(
                A(
                    Div('API Reference', cls='flex justify-between items-center w-full'),
                    href='#',
                    id='uk-nav-11',
                    role='button',
                    aria_controls='uk-nav-12',
                    aria_expanded='false',
                    aria_disabled='false'
                ),
                Ul(
                    Li(
                        A('Accordion | Link', href='#', hx_get='/api_ref/docs_accordion_link', hx_push_url='true', hx_target='#content', cls=''),
                        role='presentation'
                    ),
                    Li(
                        A('Button | Link', href='#', hx_get='/api_ref/docs_button_link', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Cards', href='#', hx_get='/api_ref/docs_cards', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Charts', href='#', hx_get='/api_ref/docs_charts', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Containers', href='#', hx_get='/api_ref/docs_containers', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Dividers', href='#', hx_get='/api_ref/docs_dividers', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Forms', href='#', hx_get='/api_ref/docs_forms', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Html', href='#', hx_get='/api_ref/docs_html', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Icons | Images', href='#', hx_get='/api_ref/docs_icons_images', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Layout', href='#', hx_get='/api_ref/docs_layout', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Lightbox', href='#', hx_get='/api_ref/docs_lightbox', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Lists', href='#', hx_get='/api_ref/docs_lists', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Loading', href='#', hx_get='/api_ref/docs_loading', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Markdown', href='#', hx_get='/api_ref/docs_markdown', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Modals', href='#', hx_get='/api_ref/docs_modals', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Navigation', href='#', hx_get='/api_ref/docs_navigation', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Notifications', href='#', hx_get='/api_ref/docs_notifications', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Sliders', href='#', hx_get='/api_ref/docs_sliders', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Steps', href='#', hx_get='/api_ref/docs_steps', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Tables', href='#', hx_get='/api_ref/docs_tables', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Theme | Headers', href='#', hx_get='/api_ref/docs_theme_headers', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Typography', href='#', hx_get='/api_ref/docs_typography', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    id='uk-nav-12',
                    role='region',
                    aria_labelledby='uk-nav-11',
                    hidden='',
                    cls='uk-nav-sub uk-nav-primary'
                ),
                cls='uk-parent'
            ),
            Li(
                A(
                    Div('Guides', cls='flex justify-between items-center w-full'),
                    href='#',
                    id='uk-nav-13',
                    role='button',
                    aria_controls='uk-nav-14',
                    aria_expanded='false',
                    aria_disabled='false'
                ),
                Ul(
                    Li(
                        A('Spacing', href='#', hx_get='/tutorial_spacing', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Layout', href='#', hx_get='/tutorial_layout', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    hidden='',
                    id='uk-nav-14',
                    role='region',
                    aria_labelledby='uk-nav-13',
                    cls='uk-nav-sub uk-nav-primary'
                ),
                cls='uk-parent'
            ),
            Li(
                A(
                    Div('Examples', cls='flex justify-between items-center w-full'),
                    href='#',
                    id='uk-nav-15',
                    role='button',
                    aria_controls='uk-nav-16',
                    aria_expanded='false',
                    aria_disabled='false'
                ),
                Ul(
                    Li(
                        A('Task', href='#', hx_get='/tasks/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Card', href='#', hx_get='/cards/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Dashboard', href='#', hx_get='/dashboard/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Form', href='#', hx_get='/forms/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Music', href='#', hx_get='/music/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Auth', href='#', hx_get='/auth/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Playground', href='#', hx_get='/playground/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Mail', href='#', hx_get='/mail/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Ticket', href='#', hx_get='/ticket/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    Li(
                        A('Scrollspy', href='#', hx_get='/scrollspy/', hx_push_url='true', hx_target='#content'),
                        role='presentation'
                    ),
                    hidden='',
                    id='uk-nav-16',
                    role='region',
                    aria_labelledby='uk-nav-15',
                    cls='uk-nav-sub uk-nav-primary'
                ),
                cls='uk-parent'
            ),
            Li(
                A('Theme', href='#', hx_get='/theme_switcher', hx_push_url='true', hx_target='#content')
            ),
            uk_nav='',
            cls='uk-nav uk-nav-primary space-y-4 p-4 w-full md:w-full'
        ),
        cls='hidden md:block w-1/5 max-w-52'
    )
    # ----------------------------------------------------------------------------
    # 2. Navbar móvil (solo en <lg): "Mi Empresa" clicable y botón menú
    #    - añadimos 'shadow-md' para sombra debajo
    mobile_navbar = Div(cls="flex items-center justify-between p-4 bg-base-200 lg:hidden shadow-md")(
        A(
            H1("Mi Empresa", cls=(TextT.lg, TextT.bold)),
            href="/home",
            hx_get="/home",
            hx_target="#main-content",
            cls="hover:underline"
        ),
        HtmlLabel(
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
    contenido_principal = Div(cls="pt-4 lg:pt-0 ml-0 lg:ml-64 p-4", id="main-content")(
        H1("Bienvenido al Dashboard", cls=(TextT.xl, TextT.bold, "mb-6")),
        P("Esta es la zona principal de la aplicación de gestión empresarial.", cls=TextPresets.muted_sm)
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
        contenido_principal,
        Script(js_toggle)
    )

    return Title("Dashboard con Sidebar"), layout


@rt(path="/home")
def home():
    # Contenido de ejemplo para "home"
    return Div(cls="space-y-4")(
        H1("Bienvenido al Dashboard", cls=(TextT.xl, TextT.bold, "mb-6")),
        P("Esta es la zona principal de la aplicación de gestión empresarial.", cls=TextPresets.muted_sm)
    )


@rt(path="/mi-zona")
def mi_zona():
    # Contenido de ejemplo para "Mi Zona"
    return Div(cls="space-y-8 p-4")(
        H2("Mi Zona", cls=(TextT.xl, TextT.bold, "mb-4")),
        # Vacaciones
        Div(cls="card bg-base-100 shadow p-4")(
            H3("Vacaciones", cls=(TextT.lg, TextT.bold, "mb-2")),
            P("Tienes 12 días de vacaciones disponibles.", cls=TextPresets.muted_sm),
            Button("Solicitar Vacaciones", cls=(ButtonT.primary, "mt-2"))
        ),
        # Nóminas
        Div(cls="card bg-base-100 shadow p-4")(
            H3("Nóminas", cls=(TextT.lg, TextT.bold, "mb-2")),
            Ul(cls="list-disc list-inside")(
                Li("Nómina Marzo 2025 - Disponible"),
                Li("Nómina Abril 2025 - Disponible"),
                Li("Nómina Mayo 2025 - Disponible")
            ),
            Button("Descargar Todas", cls=(ButtonT.secondary, "mt-2"))
        ),
        # Fichajes
        Div(cls="card bg-base-100 shadow p-4")(
            H3("Fichajes", cls=(TextT.lg, TextT.bold, "mb-2")),
            Ul(cls="list-disc list-inside")(
                Li("01/06/2025 08:59 - Entrada"),
                Li("01/06/2025 18:02 - Salida"),
                Li("02/06/2025 09:05 - Entrada"),
                Li("02/06/2025 17:58 - Salida")
            ),
            Button("Ver Historial Completo", cls=(ButtonT.secondary, "mt-2"))
        )
    )


if __name__ == "__main__":
    serve()
