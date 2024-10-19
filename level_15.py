# Algoritmo que solicite un numero entero positivo y determine si cada numero es primo o n
from math import *
numero = int(input("Introduce un numero entero positivo : "))
es_primo = 1
for i in range(2, int(sqrt(numero)+1)):
    if numero % i == 0 :
        es_primo = 0
        break
if es_primo:
    print(f"{numero} es un numero primo")
else :
    print(f"{numero} no es un numero primo")
    