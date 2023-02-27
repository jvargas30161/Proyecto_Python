#Otro ejemplo reutilizando un dato de la función, usandolo fuera de la fucnión.

# global nombre  Sin usar global si me funciona llamando la variable fuera de la función.
def saludamos():
    global nombre
    global apellido
    global edad
    nombre   = "Jorge Alexander"
    apellido = "Vargas Sánchez"
    edad = 47
    return ("Hola desde la función saludar", nombre, apellido, edad)
    # return("Hola", nombre)
    # return("Hola", apellido)
    # return("tu edad es", edad)
print(saludamos())      # también podemos imprimir por pantalla colocando print mas el valor, sin
                            #   print no hay resultado
valor = saludamos()       # Podemos trabajar llamando a una variable e imprimimos la variable.
print (valor)
# print("Hola desde fuera de la función", nombre)


