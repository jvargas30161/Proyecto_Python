# Practica 02: Descuentos de un restaurante Parte 02
# Enunciado: debido a los excelentes resultados, el restaurante decide ampliar sus ofertas
# de acuerdo a la siguiente escala de consumo, ver la tabla. Determinar el monto del descuento,
# el importe del impuesto y el importe a pagar.
#   •	Consumo (S/.)       Descuento (%)
#   •	Hasta 100                   10
#   •	Mayor a 100                 20
#   •	Mayor a 200                 30
#
# Análisis: para la solución de este problema, se requiere que el usuario ingrese el consumo y el
# sistema verifica y calcula el monto del descuento, el impuesto y el importe a pagar.

#Entrada:
consumo = float(input("Ingrese el consumo del cliente: "))

if consumo >= 0:

    ##Proceso:
    if consumo <= 100:
        #Descuento del 10%
        dato_descuento = "10%"
        descuento = consumo * 0.10
    elif consumo > 100 and consumo <= 200:
        #aplica descuento del 20%
        dato_descuento = "20%"
        descuento = consumo * 0.20
    elif consumo > 200:
        #aplica descuento del 30%
        dato_descuento = "30%"
        descuento = consumo * 0.30

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

else:
    print("==Error al ingresar el consumo, no aceptan datos negativos==")









