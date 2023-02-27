#### args lo usamos para cuando usemos argumentos por pisición.
##Primer ejemplo
print("==========Primer ejemplo básico muestra los datos como una tupla==========")

def sumar(*args):
    print(args)
    
sumar(1,2,3,4,5,6,7,8,9)


## Segundo ejemplo
print("==========Segundo  ejemplo suma los datos de la tupla==========")

def sumar(*args):
    suma =0
    for n in args:
        suma += n
    return suma

suma_total = sumar(10,20,30,40,50,60,70,80,90,100)
print("La suma total es: ", suma_total )

## Tercer ejemplo
print("==========Tercer ejemplo colocará los datos para arg por posición como por nombre ==========")

def sumar(*args, **kwargs):
    suma =0
    for n in args:
        suma += n
    return suma, kwargs

suma_total, datos  = sumar(100,202,340,940,590,609,790,850,890,10, nombre = "Jorge", edad = 47)
print("La suma total es: ", suma_total )
print(datos)




