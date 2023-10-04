import math

def area_circulo(r):
    a = round((math.pi)*(r**2),3)
    return a
#Conociendo el radio
r = 5

resultado = area_circulo(r)
print(f'El Area del circulo con radio {r} es de: {resultado}')