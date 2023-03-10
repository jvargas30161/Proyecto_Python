# Adivina el numero

import random

def jugar(vidas):
    numero_random = random.randint(1,100)
    numero_elegido = None

    while numero_random != numero_elegido:
        numero_elegido = int(input("Ingrese un numero entre 1 y 100: "))

        if numero_random < numero_elegido:
            print("Elige un numero más pequeño")
            vidas -= 1
        elif numero_random > numero_elegido:
            print("Elige un numero mas grande")
            vidas -= 1

        if vidas == 0:
            print("Game Over :(")
            break

        print(f"Te quedan {vidas} vidas ")

    if numero_elegido == numero_random:
        print("Felicidades Ganaste Brother")
        
jugar(10)

        


