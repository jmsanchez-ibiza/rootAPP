# isort: off
from fasthtml.common import *
from monsterui.all import *
# isort: on

import json
import uuid


''' def rowButton(accion: str, url: str, target: str, icon: str, color: str, scroll_to_id: str = None, disabled: bool = False):
    """Crea un botón de acción común con icono y color específico para las filas de tablas."""
    boton = Button(
        cls=f"bg-secondary text-white px-1 mx-1 border border-secondary border-1 rounded" if disabled
        else f"bg-{color} text-white px-1 mx-1 border border-{color} border-1 rounded",
        hx_get=url if url else "#",
        hx_target=f"#{target}" if target else "none",
        hx_trigger="click",
        onclick=f"scrollToId('{scroll_to_id}')" if scroll_to_id else "",
        disabled=disabled,
    )(
        I(
            cls=f"{icon} text-black fs-7" if disabled else f"{icon} text-white fs-7",
            title="No disponible" if disabled else accion.capitalize(),
            disabled=disabled
        )
    )
    return boton
'''

''' def ConfirmButton(
    texto: str,
    url: str,
    target: str,
    mensaje: str,
    titulo: str = "¿Estás seguro?",
    tipo_alerta: str = "question",
    method: str = "POST",
    data_vals: dict = None,
    submit_o_button: str = "button",
    cls: str = "btn btn-primary",
    disabled: bool = False,  # Nuevo argumento
):
    boton_id = f"btn-real-{uuid.uuid4().hex[:8]}"
    attrs = {
        "id": boton_id,
        f"hx_{method.lower()}": url,
        "hx_target": target,
        "type": submit_o_button,
        "cls": "d-none",
    }

    if data_vals:
        attrs["hx_vals"] = json.dumps(data_vals)  # ✅ este es el cambio clave

    return Div(
        # Botón visible que lanza el SweetAlert
        Button(
            type="button",
            cls=f"{cls} disabled" if disabled else cls,  # Añadimos "disabled" si está deshabilitado
            onclick=(
                f"confirmarHTMXAccion_click('{boton_id}', `{titulo}`, `{mensaje}`, '{tipo_alerta}')"
            ) if not disabled else "",  # Deshabilitamos el onclick si está deshabilitado
            disabled=disabled  # Atributo HTML disabled
        )(texto),

        # Botón oculto que realiza la acción HTMX
        Button(**attrs)()
    )
'''

''' def ConfirmDownloadButton(
    url: str,
    mensaje: str,
    titulo: str = "¿Estás seguro?",
    tipo_alerta: str = "info",
    cls: str = "btn btn-success",
    children=None,
):
    boton_id = f"btn-download-{uuid.uuid4().hex[:8]}"
    children = children or []

    return Div(
        # Botón visible con confirmación
        Button(
            type="button",
            cls=cls,
            onclick=(
                f"confirmarHTMXAccion_click('{boton_id}', `{titulo}`, `{mensaje}`, '{tipo_alerta}')"
            )
        )(*children),

        # Botón oculto que lanza la descarga
        Button(
            id=boton_id,
            type="button",
            cls="d-none",
            onclick=f"window.location.href='{url}'"
        )()
    )
'''

def ConfirmRedirectLink(
    url: str,
    mensaje: str,
    titulo: str = "¿Estás seguro?",
    tipo_alerta: str = "question",
    cls: str = "btn btn-danger",
    tooltip: str = "",
    placement: str = "bottom",
    children=None
):
    link_id = f"link-redirect-{uuid.uuid4().hex[:8]}"
    children = children or []

    attrs = {
        "type": "button",
        "cls": cls,
        "onclick": (
            f"confirmarHTMXAccion_click('{link_id}', `{titulo}`, `{mensaje}`, '{tipo_alerta}')"
        )
    }

    if tooltip:
        # attrs["data_bs_toggle"] = "tooltip"
        # attrs["title"] = tooltip
        # attrs["data_bs_placement"] = placement
        attrs["uk_tooltip"] = f"title: {tooltip}; pos: {placement}"

    return Div(
        Button(**attrs)(*children),
        A(
            href=url,
            id=link_id,
            cls="d-none"
        )()
    )


