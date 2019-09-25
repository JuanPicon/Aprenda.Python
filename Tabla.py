Numero_dado = input("Escribe un número del 1 al 10: ")
Numero_dado = int(Numero_dado)


for i in range (1,11):
    salida = "{} x {} = {}"
    print(salida.format(Numero_dado,i,i*Numero_dado))
