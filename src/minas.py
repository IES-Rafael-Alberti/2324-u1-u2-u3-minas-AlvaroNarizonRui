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
    Las celdas vacias se representan con una cadena vacia : ""
    Las banderas se representan con: "F"
    """
    tablero = generarTablero()
    generarMinas(tablero)
    

def generarTablero():
    tablero = [[".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."],
               [".",".",".",".",".",".",".","."]]
    return tablero

    
def generarMinas(tablero:list):
    """
    Inserta 10 minas de forma aleatoria sobre un tablero de buscaminas de 8x8.
    Mientras el numero de minas sea mayor que 0, se añadirá una mina en una posición 
    aleatoria.

    :param tablero: El tablero de juego donde se va a añadir las minas
    :type tablero: list.
    """
    NUMEROMINAS = 10
    while NUMEROMINAS > 0:
        posicion_x = random.randint(0,7)
        posicion_y = random.randint(0,7)
        tablero[posicion_y].insert(posicion_x,"*")
        NUMEROMINAS -= 1

            


#def generarNumerosAbyacentes():




if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
