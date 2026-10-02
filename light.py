##Codigo creado por Kevin Fajardo Sepulveda y Jorge Salcido Peralta

import os
import random 
import time

import comandos_consola as consola
import impresiones as imp

# ==========================================
# CONFIGURACIÓN Y ESTILOS
# ==========================================

COLORES_HEX = ["0969da", "eda73b", "8b9bb4", "e43b44", "44ba2d"]

# ==========================================
# LÓGICA DEL JUEGO
# ==========================================

def dibujar_menu():
    """Dibuja la cuadrícula vacía."""
    consola.cls_limpiar_pantalla()
    # Asegurar que el suelo se dibuje con el color por defecto
    consola.cls_restaurar_colores() 
    imp.crear_menu()

def dibujar_controles(dif):
    # Asegurar que el suelo se dibuje con el color por defecto
    consola.cls_restaurar_colores() 
    imp.imprimir_instrucciones(dif)

def dibujar_tablero(matriz,dif):
    """Dibuja la cuadrícula vacía."""
    consola.cls_limpiar_pantalla()
    # Asegurar que el suelo se dibuje con el color por defecto
    consola.cls_restaurar_colores() 
    color=""
    for i in range(1,dif+1):
        for j in range(1,dif+1):
            if matriz[i-1][j-1]:
                imp.dibujar_lampara_enc(i,j,color,dif)
            else:
                imp.dibujar_lampara(i,j,color,dif)

def dibujar_tablero_jug(matriz,dif):
    """Dibuja la cuadrícula vacía."""
    # Asegurar que el suelo se dibuje con el color por defecto
    consola.cls_restaurar_colores() 
    color=""
    for i in range(1,dif+1):
        for j in range(1,dif+1):
            if matriz[i-1][j-1]:
                imp.dibujar_lampara_enc(i,j,color,dif)
            else:
                imp.dibujar_lampara(i,j,color,dif)

def borrar_rastro(fila, columna, matriz, dif):
    """Dibuja un bloque de suelo normal donde estaba el personaje."""
    consola.cls_mover_cursor(fila, columna)
    consola.cls_restaurar_colores() # Asegurar color por defecto para el suelo
    if matriz[fila-1][columna-1]:
        imp.dibujar_lampara_enc(fila, columna, "", dif)
    else:
        imp.dibujar_lampara(fila, columna, "", dif)

def dibujar_personaje(fila, columna, color_hex, matriz,dif):
    """Calcula la posición visual, aplica el color y dibuja al personaje."""
    consola.cls_mover_cursor(fila, columna)
    # 1. Activamos el color especial antes de imprimir.
    # 2. Imprimimos el personaje.
    if matriz[fila-1][columna-1]:
        imp.dibujar_lampara_enc(fila, columna, color_hex,dif)
    else:
        imp.dibujar_lampara(fila, columna, color_hex,dif)
    # 3. Es importante restaurar colores inmediatamente para no "pintar" el resto de los caracteres en consola.
    consola.cls_restaurar_colores()

def borrar_rastro_menu(fila):
    #columna_visual = (columna * 2) - 1
    """Dibuja un bloque de suelo normal donde estaba el personaje."""
    consola.cls_restaurar_colores() # Asegurar color por defecto para el suelo
    imp.dibujar_seleccion_per(fila,"")

def dibujar_personaje_menu(fila, color_hex):
    #columna_visual = (columna * 2) - 1
    """Calcula la posición visual, aplica el color y dibuja al personaje."""
    # 1. Activamos el color especial antes de imprimir.
    # 2. Imprimimos el personaje.
    imp.dibujar_seleccion_per(fila,color_hex)
    # 3. Es importante restaurar colores inmediatamente para no "pintar" el resto de los caracteres en consola.
    consola.cls_restaurar_colores()

def cambiar_estado(fila, columna, matriz, matriz_auxiliar, dif):
    j = -1
    while j < 2:
        if 0 <= fila + j <= dif-1:
            matriz[fila+j][columna] = not matriz[fila+j][columna]
        if j != 0 and 0 <= columna + j <= dif-1:
            matriz[fila][columna+j] = not matriz[fila][columna+j]
        j += 1
    matriz_auxiliar[fila][columna] = not matriz_auxiliar[fila][columna]

def modo_ayuda(color_hex, matriz, matriz_auxiliar,dif):
    for x in range(dif):
        for y in range(dif):
            if matriz_auxiliar[x][y]==True:
                dibujar_personaje(x+1, y+1, color_hex, matriz,dif)
                #matriz_auxiliar[x][y]=False
                return 0

def imprimir_menu(color):
    imp.crear_menu(color)
    

def logica_menu():
    

    fila=1
    columna=1
    color=COLORES_HEX[3]
    color_actual=COLORES_HEX[3]

    consola.cls_limpiar_pantalla()
    imp.dibujar_seleccion_dif1()
    imp.dibujar_seleccion_dif2()
    imprimir_menu(color_actual)
    

    dibujar_personaje_menu(fila,color_actual)
    while True:

            comando = consola.cls_leer_tecla()

            if comando == "NADA":
                nuevo_color = random.choice(COLORES_HEX)
                # Opcional: Asegurar que el color sea diferente al actual.
                while nuevo_color == color_actual:
                    nuevo_color = random.choice(COLORES_HEX)
                
                color_actual = nuevo_color

                time.sleep(0.5)

                imprimir_menu(color_actual)

            if comando == "ENTER":
                if fila == 1:
                    return 5
                elif fila == 2:
                    return 7
                elif fila == 3:
                    return 9
                
            fila_ant, col_ant = fila, columna

            if comando == "ARRIBA":
                fila = max(1, fila - 1)
            elif comando == "ABAJO":
                fila = min(3, fila + 1)

            if fila != fila_ant:
                borrar_rastro_menu(fila_ant)
                dibujar_personaje_menu(fila,color)

# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def iniciar_juego():
    # Preparación
    os.system("") 
    consola.cls_ocultar_cursor()

    dif=logica_menu()

    matriz = [[False for _ in range(dif)] for _ in range(dif)]
    matriz_auxiliar = [[False for _ in range(dif)] for _ in range(dif)]
    i = 0
    while i < dif-1:
        x = random.randint(0, dif-1)
        y = random.randint(0, dif-1)
        if matriz_auxiliar[x][y] == False:
            #matriz_auxiliar[x][y] = True
            cambiar_estado(x, y, matriz, matriz_auxiliar, dif)
            i+=1

    dibujar_tablero(matriz,dif)
    dibujar_controles(dif)
    imp.dibujar_titulo()

    fila = 1
    columna = 1
    color=COLORES_HEX[3]
    color2=COLORES_HEX[4]

    dibujar_personaje(fila,columna,color,matriz,dif)

    #consola.cls_mover_cursor(1,1)
    #print(matriz_auxiliar)

    try:    

        while True:
            fin = 0
            for x in range (dif):
                for y in range (dif):
                    if matriz[x][y]:
                        fin +=1

            comando = consola.cls_leer_tecla()
            
            # LÓGICA DEL COLOR.
            if comando == "ENTER":
                cambiar_estado(fila-1, columna-1, matriz, matriz_auxiliar, dif)
                dibujar_tablero_jug(matriz,dif)
                dibujar_personaje(fila, columna, color, matriz, dif)
                continue # Saltamos el resto del ciclo.

            if comando == "BACKSPACE":
                modo_ayuda(color2, matriz, matriz_auxiliar,dif)
                #consola.cls_mover_cursor(1,1)
                #print(matriz_auxiliar)
                continue # Saltamos el resto del ciclo.

            if comando == "SALIR":
                break

            # LÓGICA DE MOVIMIENTO.
            fila_ant, col_ant = fila, columna

            if comando == "ARRIBA":
                fila = max(1, fila - 1)
            elif comando == "ABAJO":
                fila = min(dif, fila + 1)
            elif comando == "DERECHA":
                columna = min(dif, columna + 1)
            elif comando == "IZQUIERDA": 
                columna = max(1, columna - 1)

            if fila != fila_ant or columna != col_ant:
                borrar_rastro(fila_ant, col_ant,matriz,dif)
                dibujar_personaje(fila,columna,color,matriz,dif)

            if fin == 0 and comando=="NADA":
                imp.imprimir_ganar(dif)
                break
    finally:
        # Limpieza final.
        consola.cls_restaurar_colores() # Importante: quitar colores antes de salir.
        consola.cls_mostrar_cursor()
        imp.dibujar_despedida(dif)


if __name__ == "__main__":
    iniciar_juego()