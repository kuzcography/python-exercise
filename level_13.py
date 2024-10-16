# Tablas de multiplicar hasta un número n
numero = int(input("Introduce un número : "))
for z in range(0, numero+1) :
    pantalla_horizontal  = f"|   {z}   |"
    if z == 0 :
        for i in range(1, numero+1):  
            pantalla_horizontal += f"   {i}   |"
    else : 
        for i in range(1, numero+1):  
            pantalla_horizontal += f"   {z*i}   |"
    print(pantalla_horizontal)