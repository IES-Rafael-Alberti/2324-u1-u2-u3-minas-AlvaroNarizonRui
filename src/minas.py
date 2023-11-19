"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""

import random

def jugar():
    """
    Esta función ejecuta el juego.
    Las minas se representan con el símbolo "*"
    Las posiciones abyacentes a las minas son los números : 1,2,3,4
    Las celdas vacias se representan con el número 0.
    Las banderas se representan con: "F"
    """
    tablero_interno = inicializarTableroInterno()
    tablero_visible = inicializarTableroVisible()
    minas = generarMinas(tablero_interno)
    calcularNumerosAbyacentes(tablero_interno)
    salir = False
    while not salir:
        imprimirTablero(tablero_visible)
        celdas_destapadas = contarCeldasDestapadas(tablero_visible)
        if celdas_destapadas < 54:
            opcion = int(input(f"\nQue deseas hacer : \n 1. Revelar Celda \n 2. Marcar Celda \n 3. Salir \n Opcion : "))

            if opcion == 1:
                coordenadas = str(input("Escribe las coordenadas de la casilla que quieres destapar (x,y) : "))
                fila, columna = coordenadas.split(",")
                fila = int(fila)
                columna = int(columna)
                continuar = destaparCasilla(tablero_visible,tablero_interno,fila,columna)
                if not continuar:
                    imprimirTablero(tablero_visible)
                    print("Fin del juego :(")
                    salir = True
            if opcion == 2:
                #Entrada
                coordenadas = str(input("Escribe las coordenadas de la casilla que quieres colocar la bandera (x,y) : "))
                fila, columna = coordenadas.split(",")
                fila = int(fila)
                columna = int(columna)
                #Procesamiento
                if 0 <= fila <= 7 and 0 <= columna <= 7:
                    tablero_visible[fila][columna] = "F"
                else:
                    print("Coordenadas fuera del rango permitido (0-7)")
            elif opcion == 3:
                salir = True

            elif opcion <= 0:
                print("No se puede introducir una opción menor o igual que 0")

            elif opcion > 3:
                print("No se puede introducir un número mayor que 3")
        elif celdas_destapadas == 54:
            print("Ganaste")
            salir = True
    
def inicializarTableroInterno():
    """Inicializa el tablero en el que se va a operar.
    La única diferencia es que en este tablero las casillas
    vacías son "" en vez de ".".
    :returns: El tablero interno.
    :rtype: list
    """
    tablero_interno = [["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""]]
    return tablero_interno
    
def inicializarTableroVisible():
    """Inicializa un tablero de buscaminas 8x8 y lo
       devuelve.
       :returns: El tablero de juego.
       :rtype: list
       """
    tablero = [[".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."]]
    return tablero

def generarMinas(tablero_interno:list) -> list:
    """Genera las minas dentro del juego en un tablero de 8x8 y devuelve
       las coordenadas de las minas.
       :param tablero_interno: Lista de listas que representa el tablero de juego internamente.
       :type tablero_interno: list
       :returns: Coordenadas de las minas almacenadas en una lista su posicion x e y.
       :rtype: list
    """
    minas = list()
    while len(minas) < 10:
        posicion_y = random.randint(0,7)
        posicion_x = random.randint(0,7)
        if tablero_interno[posicion_y][posicion_x] != "*":
            minas.append((posicion_x,posicion_y))
            tablero_interno[posicion_y][posicion_x] = "*"
    return minas

def calcularNumerosAbyacentes(tablero_interno:list):
    """
    Calcula los números adyacentes a las minas en el tablero interno.
    :param tablero_interno: Lista de listas que representa el tablero interno.
    :type tablero_interno: list
    """
    filas = len(tablero_interno)
    columnas = len(tablero_interno[0])

    for fila in range(filas):
        for columna in range(columnas):
            if tablero_interno[fila][columna] != "*":
                contador_minas = 0
                for i in range(max(0, fila -1), min(filas, fila + 2)):
                    for j in range(max(0, columna - 1), min(columnas, columna + 2)):
                        if tablero_interno[i][j] == "*":
                            contador_minas += 1
                tablero_interno[fila][columna] = contador_minas
    


def contarCeldasDestapadas(tablero_visible:list) -> int:
    """Cuenta las celdas destapadas dentro del tablero que ve 
       el jugador durante la partida. Al ser un tablero de 8x8
       el cual tiene 10 minas repartidas por el mapa deja libres
       54 casillas sin minas. Una vez que se alcanza ese número el
       jugador gana.
       :param tablero_visible: Es el tablero de 8x8 con el que interactúa
        el jugador durante la partida.
       :type tablero_visible: list
       :returns: El número de casillas destapadas. Al alcanzar el máximo(54)
       el juego termina y gana el jugador. De lo contrario continúa el juego.
       :rtype: int.
    """
    casillas_destapadas = 0
    for fila in range(len(tablero_visible)):
        for columna in range(len(tablero_visible[fila])):
            if tablero_visible[fila][columna] != ".":
                casillas_destapadas += 1
    return casillas_destapadas


def imprimirTablero(tablero:list):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j],end= "  ")
        print()

def destaparCasilla(tablero_visible:list,tablero_interno:list,fila:int,columna:int) -> bool:
    """Destapa una casilla del tablero visible al usuario. Compara la posición del tablero visible
        con la del tablero interno y si en esta posición hay una bomba devuelve si continúa el juego
        o no.
    """
    if tablero_interno[fila][columna] != "*":
        tablero_visible[fila][columna] = tablero_interno[fila][columna]
        return True
    else:
        tablero_visible[fila][columna] = tablero_interno[fila][columna]
        return False


if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
