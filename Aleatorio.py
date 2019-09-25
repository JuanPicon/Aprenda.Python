import random

PrimerNumero = float(10.5)

def Mifuncion():
    SegundoNumero = float(random.randrange(1,10))
    Texto = "La suma de {} y {} es {}"
    print(Texto.format(PrimerNumero,SegundoNumero,PrimerNumero+SegundoNumero))

Mifuncion()