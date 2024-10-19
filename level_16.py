# El algoritmo muestra una matriz NxN utilizando 2 bucles for
numero = int(input("Introduce un numero : "))
for i in range(0, numero) :
    disp = ""
    for e in range(0, numero) :
        if e == i:
            disp += " O "
        elif e < i :
            disp += " * "
        else :
            disp += " + "
    print(disp)
