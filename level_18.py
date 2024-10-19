# El programa genera un número aleatorio y utiliza un bucle infinito hasta que la utilidad encuentra el número correcto
import random
numero_aleatorio = random.randint(1, 100)
cantidad_de_intentos = 0
while True :
    numero = int(input("Introduce un numero : "))
    cantidad_de_intentos += 1
    if numero < numero_aleatorio:
        print("Es menor")
    elif numero > numero_aleatorio:
        print("Es major")
    elif numero == numero_aleatorio:
        print(f"Tienes el número correcto con {cantidad_de_intentos} intentos")
        break
