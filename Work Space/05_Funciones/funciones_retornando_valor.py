#Otro ejemplo reutilizando un dato de la función, usandolo fuera de la fucnión.

# global nombre  Sin usar global si me funciona llamando la variable fuera de la función.
def saludamos():
    global nombre
    nombre = "Jorge Alexander"
    apellido = "Vargas Sánchez"
    edad = 47
    return ("Hola desde la función saludar")
    return("Hola", nombre)
    return("Hola", apellido)
    return("tu edad es", edad)
saludamos()
# print("Hola desde fuera de la función", nombre)


