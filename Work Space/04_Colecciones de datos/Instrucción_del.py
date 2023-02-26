# instrucción DEL se puede usar para eliminar elementos e una lista o diccionario, o eliminar un
# trozo de una lista o vaciar toda la lista.

a = ["a","b","c","d","e","f"]
print(a)
#Con esta función estoy eliminando datos de la lista.
del a[0]
del a[0]
print(a)
#Con esta función puedo pedir que solo se muestre un trozo de la lista.
del a[:3]
print(a)

#Con esta función puedo vaciar la lista.
del a[:]
print(a)

# # #Con esta función puedo eliminar la lista.
# del a
# print(a)

# #Con esta función puedo eliminar la lista de los diccionarios.
d = {"uno":1,"dos":2,"tres":3, }
del d["dos"]
print(d)

# #Con esta función puedo eliminar lla definición del diccionario.
del d
print(d)







