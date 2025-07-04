import inspect

def debug_pause(msg):
    # Obtiene el frame anterior en la pila de llamadas
    frame = inspect.currentframe().f_back
    filename = frame.f_code.co_filename
    func_name = frame.f_code.co_name

    msg = f"DEBUG-PAUSE: ({filename}) ({func_name})\n{msg}"
    input(msg)

def debug_print(*args):
    # Obtiene el frame anterior en la pila de llamadas
    frame = inspect.currentframe().f_back
    # Obtiene el nombre del archivo donde se llamó la función
    filename = frame.f_code.co_filename
    # Obtiene el nombre de la función desde donde se llamó
    func_name = frame.f_code.co_name
    # Construye un mensaje con información de depuración y los argumentos recibidos
    msg = f"DEBUG-PRINT ({filename}, {func_name}): " + ", ".join(
        f"{name}={value!r}" for name, value in zip(debug_pause.__code__.co_varnames, args)
    )
    # Añade una representación en string de los argumentos (excepto el primero)
    msg += "\n" + "\n".join(str(arg) for arg in args[1:])
    # Pausa la ejecución esperando una entrada del usuario
    print(msg)