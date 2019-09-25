Numero1 = input("Dame un número: ")
Numero2 = input("Dame otro número: ")
Numeros = ("Numeros dados: {} y {}. {}.")

if(Numero1>Numero2):
    print(Numeros.format(Numero1, Numero2, "El primer número es mayor al segundo"))
else:
    if Numero1<Numero2:
        print (Numeros.format(Numero1, Numero2, "El primer número es menor al segundo"))
    else:
        print (Numeros.format(Numero1, Numero2, "Los dos números son iguales"))

