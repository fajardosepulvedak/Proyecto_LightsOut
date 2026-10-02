import sys
import msvcrt

def cls_imprimir(texto):
    """Imprime texto inmediatamente en pantalla sin hacer salto de línea."""
    sys.stdout.write(texto)
    sys.stdout.flush()

def cls_mover_cursor(fila, columna):
    """Mueve el cursor a una posición específica de la terminal."""
    cls_imprimir(f"\033[{fila};{columna}H")

def cls_ocultar_cursor():
    """Oculta el cursor parpadeante."""
    cls_imprimir("\033[?25l")

def cls_mostrar_cursor():
    """Muestra nuevamente el cursor."""
    cls_imprimir("\033[?25h")

def cls_limpiar_pantalla():
    """Borra todo el contenido de la consola."""
    cls_imprimir("\033[2J\033[H")

def cls_restaurar_colores():
    """Vuelve a los colores por defecto de la terminal."""
    cls_imprimir("\033[0m")

def cls_establecer_color_hex(hex_color):
    """
    Toma un color hexadecimal y aplica color 'True Color' (24 bits)
    al texto de la consola usando el código ANSI: \033[38;2;R;G;Bm
    """
    # 1. Convertir Hex (base 16) a RGB (base 10).
    # [0:2] toma los primeros dos caracteres, int(..., 16) lo convierte a entero base 10
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    # 2. Aplicar el código ANSI True Color.
    cls_imprimir(f"\033[38;2;{r};{g};{b}m")

def cls_leer_tecla():
    """
    Lee la tecla y la traduce.
    """
    if not msvcrt.kbhit(): # Esperar a que el usuario presione alguna tecla.
        return "NADA" 
    
    tecla = msvcrt.getch()

    # Detectar ENTER.
    if tecla == b'\r':
        return "ENTER"

    # Detectar BACKSPACE
    if tecla == b'\x08':
        return "BACKSPACE"

    # Detectar Flechas (son códigos de dos bytes).
    #if tecla in (b'\x00', b'\xe0'):
    #    flecha = msvcrt.getch()
    #    if flecha == b'H': return "ARRIBA"
    #    if flecha == b'P': return "ABAJO"
    #    if flecha == b'M': return "DERECHA"
    #    if flecha == b'K': return "IZQUIERDA"

    if tecla == b'w': 
        return "ARRIBA"
    if tecla == b's': 
        return "ABAJO"
    if tecla == b'd': 
        return "DERECHA"
    if tecla == b'a': 
        return "IZQUIERDA"
    if tecla.lower() == b'i':# or tecla == b'\x1b'
        return "INICIAR"
    
    # Detectar SALIR.
    if tecla.lower() == b'q' or tecla == b'\x1b':
        return "SALIR"

    return "OTRA"

def cls_leer_tecla_Salir():
    """
    Lee la tecla y la traduce.
    """
    if not msvcrt.kbhit(): # Esperar a que el usuario presione alguna tecla.
        return "NADA" 

    tecla = msvcrt.getch()

    # Detectar SALIR.
    if tecla.lower() == b'q' or tecla == b'\x1b':
        return "SALIR"

    return "OTRA"