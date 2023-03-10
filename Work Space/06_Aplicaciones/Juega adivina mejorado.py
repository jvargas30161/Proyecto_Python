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
        
def main():
    while True:
        menu = """
        ADIVINA EL NUMERO ALEATORIO
         1 - Nivel fácil
         2 - Nivel Intermedio 
         3 - Nivel Difícil
         4 - Salir
         INGRESE UNA OPCION """

        opcion = input(menu)

        if opcion == "1":
            jugar(10)
        if opcion == "2":
            jugar(7)
        if opcion == "3":
            jugar(5)
        if opcion == "4":
            print("Cerrando el Juego")
            break
        else: 
            print("Opción incorrecta, vuelva a ingresar")



if __name__ == '__main__':
    main()
        


