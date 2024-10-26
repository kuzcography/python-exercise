import math
a = int(input("Ingrese el coeficiente a: "))
b = int(input("Ingrese el coeficiente b: "))
c = int(input("Ingrese el coeficiente c: "))
discriminante = b**2 - 4*a*c
if discriminante < 0:
    print("La ecuación no tiene solución en los números reales.")
elif discriminante == 0:
    raiz = -b / (2*a)
    print(f"La ecuación tiene una solución única: {raiz:.2f}")
else:
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"La ecuación tiene dos soluciones reales: {raiz1} y {raiz2}")