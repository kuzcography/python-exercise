# Muestra asteriscos o sumas según sean pares o impares
numero_base = int(input("Introduce un número (base) : "))
numero_altura = int(input("Introduce un número (altura) : "))
base_asterisco = ""
base_suma = ""
for i in range(numero_base):
    base_asterisco += "*"
    base_suma += "+"
for i in range(1, numero_altura + 1) :
    if i%2 == 0 :
        print(base_suma)
    elif i%2 == 1:
        print(base_asterisco)