edad = int(input("Ingrese la edad: "))
if 0 < edad < 2:
    grupo_edad = "Bebé"
elif 2 <= edad < 12:
    grupo_edad = "Niño"
elif 12 <= edad < 18:
    grupo_edad = "Adolescente"
elif 18 <= edad < 30:
    grupo_edad = "Adulto Joven"
elif 30 <= edad < 65:
    grupo_edad = "Adulto"
elif edad >= 65:
    grupo_edad = "Tercera Edad"
else:
    grupo_edad = "Edad no válida"
print(f"El grupo de edad es: {grupo_edad}")