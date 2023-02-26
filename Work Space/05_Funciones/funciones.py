#las funciones se definen con palabra reservada def y se finaliza con ():

#Ejemplo
print("====================Un ejemplo usando funciones ======================")

def saludar():
    print("Hola desde la función saludar") #En este caso esta función no se está devolviendo nada
                                        #porque no estamos llamando a la función. Importante, primero se definen
saludar()

#Otro ejemplo
print("====================Un ejemplo usando funciones ======================")

def saludamos():
    nombres = "Jorge Alexander"
    apellidos = "Vargas Sánchez"
    edad = 47
    print("Hola desde la función saludar")
    print("Hola", nombres)
    print("Hola", apellidos)
    print("tu edad es", edad)
saludamos()

print("====================Un ejemplo usando funciones ======================")
#Otro ejemplo reutilizando un dato de la función, usandolo fuera de la fucnión.

# global nombre  Sin usar global si me funciona llamando la variable fuera de la función.
def saludamos():
    global nombre
    nombre = "Jorge Alexander"
    apellido = "Vargas Sánchez"
    edad = 47
    print("Hola desde la función saludar")
    print("Hola", nombre)
    print("Hola", apellido)
    print("tu edad es", edad)
saludamos()
print("Hola desde fuera de la función", nombre)


