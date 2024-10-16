# algoritmo babilónico, para calcular la raíz cuadrada de un número, cuantas más iteraciones haya, más preciso será el resultado.
numero = int(input("Introduce un número: "))
iteracion = int(input("Introduce un número: "))
raiz_cuadrada = 0
resultado_iteracion = 0
for i in range(iteracion) :
    if i == 0 :
        resultado_iteracion = numero/2
    else :
        resultado_iteracion = 1/2 * (resultado_iteracion + 25 / resultado_iteracion)
    print(f"Resultado de la iteración n{i} : {resultado_iteracion}")
