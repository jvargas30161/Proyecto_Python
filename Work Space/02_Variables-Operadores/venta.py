"""Practica 02: Calcular el Precio de Venta
Enunciado: dado el valor de venta de productos, hallar el IGV (18%) y el precio de venta.
Análisis: para la solución de este problema, se requiere que el usuario ingrese el valor de venta del producto y el
sistema realice el cálculo respectivo para hayar el IGV y el precio de venta, para esto use la siguiente expresión.
igv = vv * 0.18
pv = vv + igv
"""

##Mensaje de la aplicación
print("-----REALIZAR UNA VENTA :) ------")

##Entrada de datos
vv = float(input("Ingrese valor de venta: " ))

##Operaciones
igv = vv * 0.18
pv = vv + igv

##Salida de datos
print ("=" * 40)
print ("=========== FACTURA DE VENTA ===========")
print ("=" * 40)
print ("Valor de Venta: ",  vv )
print ("           Igv: ", igv )
print ("Precio de Venta: ", pv )
print ("=" * 40)




