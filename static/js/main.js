// Código JS

// Para pedir una confirmación antes de una acción
// Ejemplo:
// Iconos: success, error, warning, info, question
function confirmarHTMXAccion_click(botonId, titulo, mensaje, tipo = 'question') {
    Swal.fire({
        title: titulo,
        text: mensaje,
        icon: tipo,
        showCancelButton: true,
        confirmButtonColor: '#198754',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, continuar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            const realButton = document.getElementById(botonId);
            if (realButton) {
                realButton.click();
            } else {
                console.warn(`Botón oculto con id "${botonId}" no encontrado.`);
            }
        }
    });
}