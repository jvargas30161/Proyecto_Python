### funciones lambda, podemos crearla para expresiones pequeñas. Se puede usar para una
# expresión pequeña.
### Primer ejemplo.
print("=================Función lambda sumar básico======================")
sumar = lambda a,b:a+b
print( sumar(10,80))

print("=================Función lambda doblar un número==================")
doblar = lambda n: n*2
print(doblar(100))


print("=================Función lambda par o impar un número==================")
par = lambda n: n % 2 ==0
impar = lambda n: n%2 !=0

print(par(901))
print(impar(45))

print("=================Función lambda funcion anonima revertir cadena==================")
revertir = lambda cadena: cadena[::-1]

print(revertir("jorge alexander"))
print(revertir("jorge alexander vargas sanchez"))




