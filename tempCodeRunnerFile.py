for i in range (1,11) :
    Texto = "Tabla del {}"
    print(Texto.format(i))

    print ()

    for j in range (1,11):

        Tabla = "{} x {} = {}"
        print(Tabla.format(i,j,i*j))
    else:
         print()