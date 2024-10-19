# El algoritmo pide el número de votos de 4 candidatos, utilizo 2 bucles, uno para sumar el número de votos de cada candidato y otro para mostrar los resultados
votos = input("Introduce todos los votos (identificadores 1, 2, 3 y 4): ")
candidatos = [0,0,0,0]
numero_de_votos = 0
for i in votos.replace(" ", ""):
    numero_de_votos += 1
    if i == "1":
        candidatos[0] += 1
    elif i == "2":
        candidatos[1] += 1
    elif i == "3":
        candidatos[2] += 1
    elif i == "4":
        candidatos[3] += 1
for i, v in enumerate(candidatos):
    print(f"candidatos {i + 1} : tienes {v} votos y {round((v/numero_de_votos)*100, 2)} por ciento ")
