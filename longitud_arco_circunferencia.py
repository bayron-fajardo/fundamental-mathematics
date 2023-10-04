import math

def arco_circunferencia(r,angulosr):
    l = round(r * angulosr, 2)
    return l

r = 10
angulosr = math.pi / 3

resultado = arco_circunferencia(r,angulosr)
print(resultado)