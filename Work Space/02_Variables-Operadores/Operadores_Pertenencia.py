## Normalmente se trabaja con listas, para saber por ejemplo si un valor pertenece o no pertenece a una lista.

print("================================= En hola mundo existe o no ===========================================")
texto = "Hola Mundo"
print("h" in texto)
print("H" in texto)
print("M" in texto)
print("la" in texto)

l = [3, 1, 2]
l.sort()
print(l)

l = ["Periphery", "Intervals", "Monuments"]
print(l.index("Intervals"))

numero = 25
print(numero)

print("=================================        Lista de nombres           ===========================================")
nombres = ["Diego", "Carlos", "Martin", "Lorena", "Natalia"]
nombres.insert(0, "Jorge")
nombres.insert(1, "Alexander")
nombres.insert(2, "Nicolás")
nombres.insert(3, "Pilar")
nombres.insert(4, "Adriana")
nombres.insert(10, "José Carlos")
nombres.insert(11, "Jorge")
print (nombres.count("Pilar"))
print(nombres)


estudiantes = ["Jose", "Raul", "Marcelo", "Raul", "Raul", "Raul", "Raul", "Raul", "Raul", "Raul", "Raul"]
print(estudiantes)
estudiantes.count("Raul")
print (estudiantes.count("Raul"))
print ("====================jose en estudiantes================")
print ("Jose" not in  estudiantes)

frutas= ["manzana", "pera", "kiwi", "banana", "pera"]
print(frutas)
print (frutas.count("pera"))

lista12 = [1, "dos", False, [45, "cien"]]
print (lista12)
print(lista12.count(1))

