# Practica 01: Descuentos de un restaurante
# Enunciado:
#           un restaurante ofrece un descuento del 10% para consumo de hasta s/. 100.00 y un
#           descuento del 20 % para consumos mayores, para ambos casos se aplica un impuesto del 19%.
#           Determinar el monto del descuento, el impuesto y el importe a pagar.
# Análisis:
#           para la solución de este problema, se requiere que el usuario ingrese el consumo y
#           el sistema verifica y calcula el monto del descuento, el impuesto y el importe a pagar.
#           monto del descuento
#           impuesto
#           importe a pagar

#Entrada:
consumo = float(input("Ingrese el consumo del cliente: "))


#Proceso:
if consumo <= 100:
    #Descuento del 10%
    dato_descuento = "10%"
    descuento = consumo * 0.10
elif consumo > 100:
    #aplica descuento del 20%
    dato_descuento = "20%"
    descuento = consumo * 0.20

monto_descuento = consumo - descuento
igv = monto_descuento * 0.19
total_pagar = monto_descuento + igv

#Salida de datos
print("="*40)
print("-----------Factura de Consumo-----------")
print("Descuento que se aplica: ", dato_descuento)
print("="*40)
print("Consumo             : ",  consumo)
print("Descuento           : ",  descuento)
print("Monto con Descuento : ",  monto_descuento)
print("Igv                 : ",  igv)
print("Total a pagar       : ",  total_pagar)
print("="*40)









