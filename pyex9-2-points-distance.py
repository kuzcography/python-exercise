import math
x1 = float(input("Ingrese la coordenada x1 del punto P1: "))
y1 = float(input("Ingrese la coordenada y1 del punto P1: "))
x2 = float(input("Ingrese la coordenada x2 del punto P2: "))
y2 = float(input("Ingrese la coordenada y2 del punto P2: "))
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distancia entre los puntos P1 y P2 es: {distancia:.2f}")