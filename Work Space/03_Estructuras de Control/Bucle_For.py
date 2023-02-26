#Normalmente se usa para iterar listas o cadena de caracteres.
print("-----Una forma de hacerlo con for :) ------")
datos = ["Alex", "Jorge", 47, 1.74, True]

for dato in datos:
    print(dato)

print("-----Una forma de hacerlo con while :) ------")
# Otra forma usando while . usamos len para contar la cantidad de elementos
c = 0
while c < len(datos):
    print(datos[c])
    c+=1

print("-----for de un rango a otro :) ------")
# con for tambien podemos que un código se ejecute de un rango a otro.

#for
for n in range(10):
    print(n)
    #print(type(n))
