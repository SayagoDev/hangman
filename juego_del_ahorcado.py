# TODO:
# 1. Limpiar Pantalla
# 2. Tiene que aparecer el título del juego y la tarima. Así como las vidas y la palabra encubierta.
#   2.1. Constante que guarde le título del juego
#   2.2. Constante que guarde las diferentes tarimas con el personaje.
#   2.3. Función que lea un archivo para extraer la palabra encubierta.
#   2.4. Funciones que imprima (palabra, tarima, titulo)
# 3. Se debe poder ingresar letras, si esta corresponde a una o mucha de la palabra se limpiara la pantalla y aparecerán escritas.
#   3.1. Función que haga el mach entre la letra ingresada y la palabra en juego
#   3.2. Si no acierta, entonces se limpiara la pantalla y se dibujara una parte del personaje, además de que se reducirá en uno la vida.
#       3.2.1 Llamar a la función que dibuja el personaje/tarima
#       3.2.2 Se llamara a la función que maneja la vida, para reducirla en uno
# 4. Debe existir una función que en cada turno revise si el jugador a ganado o no.
#   4.1. Si gana, entonces se limpia la pantalla y aparece un mensaje de victoria
#   4.2. Si pierde sucede exactamente lo mismo pero con un mensaje de derrota.

import os
import time


# ---------------- Sprites
HANGMAN_TITLE = \
"""
  ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
  ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
  ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
  ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
  ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
                    by Saúl Sáyago
"""

HANGMAN_PICS = ['''  +---+
  |   |
      |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def get_player_name():
    time.sleep(.3)
    print("\tBienvenido al juego del ahorcado ¿_____?")
    name = input("\nIngresa tu nombre de usuario: ")
    return name


def print_player_name():
    global player_name
    global name

    if not player_name:
        name = get_player_name()
        player_name = True
    else:
        time.sleep(.3)
        print(f"\tBienvenido al juego del ahorcado {name}")


player_name = False
name = ""

def draw():
    exit = False

    while not exit:
        os.system("clear")
        print(HANGMAN_TITLE)
        print_player_name()

        exit = True if input("¿Salir? y/n --> ") == "y" else False


def run():
    draw()


if __name__ == '__main__':
    run()
