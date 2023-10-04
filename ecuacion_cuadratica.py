import math

def ecuacion_cuadratica(a,b,c):
    x1 = (-b+math.sqrt((b*b)-(4*a*c)))/(2*a)
    x2 = (-b-math.sqrt((b*b)-(4*a*c)))/(2*a)
    return x1, x2

a = 2
b = -7
c = 3

resultado = ecuacion_cuadratica(a,b,c)
print(f'El resultado es (x_1,x_2): {resultado}')