# Este código calcula el coste de una llamada telefónica en función de la duración y el tipo de llamada (internacional, nacional o local) y, a continuación, muestra el resultado. 
while True :
    typo = input("Introduce el typo de llamada (internacional, nacional, local, x): ")
    costo = 0
    if typo == "x":
        break
    duracion = int(input("Introduce la duración en  minutos : "))
    if typo == "internacional" :
        if duracion <= 2 :
            costo = duracion*3.49
        else :
            costo = duracion*3.49 + (duracion-2)*1.99   
    elif typo == "nacional" :
        if duracion <= 2 :
            costo = duracion*1.49
        else :
            costo = duracion*1.49 + (duracion-2)*0.49
    elif typo == "local" :
        costo = duracion*0.80
    print(f"El coste es de {costo}")
    