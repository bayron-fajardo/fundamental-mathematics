import math
def teora_pitagoras(a,b):
    c = math.sqrt((a**2)+(b**2))
    return c

a = 3
b = 4

resultado = teora_pitagoras(a,b)
print(f'El valor de la hipotenuso con los lados A: {a}, B: {b}, es de : {resultado}')