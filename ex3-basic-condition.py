A = int(input("Ingrese número A: "))
B = int(input("Ingrese número B: "))
C = int(input("Ingrese número C: "))
if A + B == C :
    print("A + B == C")
elif A + C == B :
    print('A + C == B')
elif B + C == A :
    print('B + C == A')
else :
    print("No iguales")