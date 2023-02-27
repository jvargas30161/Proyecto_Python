## Práctica 01: Palíndromo
# 	Crear un sistema que detecte si una palabra es palíndroma o no
# 	Para solucionar este problema el usuario tiene que ingresar por pantalla una palabra y el
# sistema verifica si es palíndromo o no.
# 	Una palabra palíndroma se lee de igual forma como de la derecha y de la izquierda.

def palindromo(palabra):

    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()

    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

#Función principal
def main():
    palabra = input("Ingrese una palabra: ")

    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print("Es palindromo")
    else:
        print("No es palindromo")

#Punto de entrada de la aplicación.
if __name__ == '__main__':
    main()