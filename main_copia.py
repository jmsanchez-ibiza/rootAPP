# main.py

from fasthtml.common import *
from monsterui.all import *

# Creamos la aplicación con tema "blue" de MonsterUI + DaisyUI activo
app, rt = fast_app(hdrs=Theme.green.headers(daisy=True))


def ex_navbar2():
    return NavBar(
        A(Input(placeholder='search')), 
        A(UkIcon("home")), 
        A('Page1',href='/rt1'), 
        A("Page2", href='/rt3'),
        brand=DivLAligned(
            UkIcon('home',height=30,width=30),
            H2("Título")
        ),
        cls="bg-gray-200 lg:p-5 p-2 lg:pr-60"
    )

@rt
def index():
    # ----------------------------------------------------------------------------
    # 1. Sidebar con sombra en el lateral derecho e inferior
    sidebar = Div(
        # cls="w-64 h-screen fixed inset-y-0 left-0 bg-base-200 text-base-content overflow-auto hidden lg:block z-20 shadow-lg",
        cls="w-64 h-screen fixed inset-y-0 left-0 bg-gray-700 text-white overflow-auto hidden lg:block z-20 shadow-lg",
        id="sidebar"
    )(
        # Logo / título de la empresa (solo visible en desktop)
        Div(cls="hidden lg:flex items-center justify-center py-6")(
            A(
                DivLAligned(
                    UkIcon('recycle',height=30,width=30),
                    H3("holded", cls="pl-2"),
                    cls="px-4"
                ),
                hx_get='/', hx_target="#main-content", onclick="hideSidebar()"
            ), cls=(TextT.lg, TextT.bold, "pb-6 pt-6")
        ),
        # "Inicio" carga el contenido de home vía HTMX
        DivHStacked(
            UkIcon(icon="home", cls="ml-4"),
            A(
                "Inicio",
                href="/home",
                cls=(TextT.bold, "ml-1"),
                hx_get="/home",
                hx_target="#main-content",
                onclick="hideSidebar()"
            ),
        ),
        
        Accordion(
            AccordionItem(
                DivHStacked(
                    UkIcon(icon="chart-bar", cls="ml-4"),
                    Span("Ventas", cls="ml-2")
                ),
                Ul(
                    Li(
                        A('Presupuestos', hx_get='/mi-zona', hx_target="#main-content", onclick="hideSidebar()", style="padding: 3px" )
                    ),
                    Li(
                        A('Pedidos', hx_get='/home', hx_target="#main-contecnt", onclick="hideSidebar()", style="padding: 3px" )
                    ),
                    hidden='',
                    id='uk-nav-ventas',
                    role='region',
                    aria_labelledby='uk-nav-label-ventas',
                    cls='uk-nav-sub uk-nav-primary !mt-0 !mb-0 !pb-0'
                ),
                cls="p-0 m-0 border-none"
            ),
            AccordionItem(
                DivHStacked(
                    UkIcon(icon="chart-bar", cls="ml-4"),
                    Span("Compras", cls="ml-2")
                ),
                Ul(
                    Li(
                        A('Facturas de compra', hx_get='/mi-zona', hx_target="#main-content", onclick="hideSidebar()", style="padding: 3px;")
                    ),
                    Li(
                        A('Pedidos de compra', hx_get='/home', hx_target="#main-content", onclick="hideSidebar()", style="padding: 3px;")
                    ),
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
            cls="space-y-0 !m-0 !p-0"  # clave para quitar separación entre ítems
        ),

        # Botón "Ver planes" al final (solo en desktop)
        Div(cls="hidden lg:block mt-3")(
                Button("Ver planes", cls=(ButtonT.primary, "w-full"))
        )
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
    contenido_principal = Div(cls="pt-4 lg:pt-0 ml-0 lg:ml-64", id="main-content")(
        ex_navbar2(),
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

    return Title("myHolded"), layout


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
            DivHStacked(
                Button("Default", cls=(ButtonT.default, "mt-20 w-64")),
                Button("Primary", cls=(ButtonT.primary, "mt-20 w-64")),
                Button("Secondary", cls=(ButtonT.secondary, "mt-20 w-64")),
                Button("Destructive", cls=(ButtonT.destructive, "mt-20 w-64")),
                Button("Text", cls=(ButtonT.text, "mt-20 w-64")),
                Button("Link", cls=(ButtonT.link, "mt-20 w-64")),
                Button("Ghost", cls=(ButtonT.ghost, "mt-20 w-64")),
            ),
        )
    )


if __name__ == "__main__":
    serve()
