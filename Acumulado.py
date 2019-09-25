Acumulado = int(0)
numero = str("")

while True:
    numero=input("Dame un número entero: ")
    if numero=="":
        print("Vacío. Saliendo del programa")
        break
    else:
        Acumulado+=int(numero)
        salida = "Monto acumulado: {}"
        print(salida.format(Acumulado))