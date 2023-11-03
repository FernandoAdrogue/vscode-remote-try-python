#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# crear un juego de piedra papel o tijera por consola
# se usa la consola para interactuar con el jugador y para mostrar la respuesta
# se usa un ciclo while para que el juego se ejecute hasta que se decida terminar
# se usa un ciclo try except para validar que la entrada sea un numero entero
# se usa un ciclo while para validar que la entrada este entre 1 y 3
# se usa un ciclo if para validar si el jugador gana, pierde o empata
# se usa un ciclo if para validar si el jugador quiere continuar jugando
# se una una variable para guardar los resultados del jugador

import random
print("Bienvenido a Piedra, Papel o Tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
print("4. Salir")

opcion = 0
resultados_jugador = []
while opcion != 4:
    while True:
        try:
            opcion = int(input("Que deseas jugar? "))
            break
        except ValueError:
            print("Debes ingresar un numero entero")

    while opcion < 1 or opcion > 4:
        print("Debes ingresar un numero entre 1 y 4")
        opcion = int(input("Que deseas jugar? "))

    if opcion == 4:
        break

    print("Tu eleccion es: " + str(opcion))

    computador = random.randint(1, 3)
    print("La eleccion del computador es: " + str(computador))

    if opcion == computador:
        print("Empate")
        resultados_jugador.append("Empate")
    elif opcion == 1 and computador == 2:
        print("Perdiste")
        resultados_jugador.append("Perdiste")
    elif opcion == 1 and computador == 3:
        print("Ganaste")
        resultados_jugador.append("Ganaste")
    elif opcion == 2 and computador == 1:
        print("Ganaste")
        resultados_jugador.append("Ganaste")
    elif opcion == 2 and computador == 3:
        print("Perdiste")
        resultados_jugador.append("Perdiste")
    elif opcion == 3 and computador == 1:
        print("Perdiste")
        resultados_jugador.append("Perdiste")
    elif opcion == 3 and computador == 2:
        print("Ganaste")
        resultados_jugador.append("Ganaste")

    opcion = int(input("Deseas continuar? (1. Si / 2. No) "))
    while opcion < 1 or opcion > 2:
        print("Debes ingresar un numero entre 1 y 2")
        opcion = int(input("Deseas continuar? (1. Si / 2. No) "))
    if opcion == 2:
        opcion = 4

print("Resultados del jugador: ", resultados_jugador)
