Numero = int(input("Dame un número entero: "))

ElMultiplo3=((Numero%3)==0)
ElMultiplo5=((Numero%5)==0)
ElMultiplo7=((Numero%7)==0)

if ((ElMultiplo3 and ElMultiplo5 ) or ElMultiplo7):
    print("Correcto.")
else:
    print ("Incorrecto. ")