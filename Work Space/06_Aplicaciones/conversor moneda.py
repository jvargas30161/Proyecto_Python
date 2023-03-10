### Aplicación básica
print ("==========Aplicación básica==========")
def convertir(valor_dolar, pais):
    cantidad_moneda = float(input(f"Ingrese cantidad de {pais}: "))

    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares, 2)
    print (f"Tienes ${dolares} Dolares")

convertir(3.61, "Soles Peruanos")


### Aplicación un poco más completa
print ("==========Aplicación un poco más completa==========")
def convertir(valor_dolar, pais):
    cantidad_moneda = float(input(f"Ingrese cantidad de {pais}: "))

    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares, 2)
    print (f"Tienes ${dolares} Dolares")

def main():

    while True:
        menu = """
        1 - Soles Peruanos    a Dolares
        2 - Pesos Mexicanos   a Dolares
        3 - Pesos Colombianos a Dolares 
        4 - Salir 
        Ingrese una Opción: """

        opcion = input(menu)
        
        if opcion == "1":
            convertir(3.61, "Soles Peruanos")
        elif opcion == "2":
            convertir(20, "Pesos Mexicanos")
        elif opcion == "3":
            convertir(3471.27, "Pesos Colombianos")
        elif opcion == "4":
            print("Cerrando Conversor de Monedas ")
            break
            print("Vuelve a ingresar la opción correcta")

## Punto de inicio de la aplicación.
if __name__ == "__main__":
    main()





