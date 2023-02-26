## estas colecciones de datos son desordenados o no se respeta un orden.
# Un conjunto no puede almacenar un valor que se repita

a = set()
print(type(a))

print("**************Datos del conjunto********************")
print("Podemos ver que se muestra desordenados")
a = {"a","e", "i", "o", "u", "b"}
print(a)


print("**************Volvemos a definir  repetimos elementos*******************")
print("Podemos ver que se muestra desordenados")
a = {"a","e", "i", "o", "u", "b", "a", "a"}
print(a)


print("**************Convertir una cadena de caracter en conjunto*******************")
a = set("abracadabra")
print(a)

b = set("alacazam")
print(b)


print("**************Trabajar con signo <menos> u otro operador en conjuntos ******************")
print(a - b)
print(a | b)
print(a & b)
# print.a ** b    ### No se ejecuta.


print("**************conjuntos con metodos ******************")
a = {"a", "b", "c"}
a.add("d")
a.add("d")
a.add("q")
a.add("q")
print(a)


print("**************eliminar un elemento******************")
a.discard("a")
print(a)


print("**************metodo clear *****************")
a.clear()
print(a)






