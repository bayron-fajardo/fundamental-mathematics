def suma_serie_aritmetica(a1, an, n):
    suma = (n * (a1 + an)) // 2
    return suma

a1 = 2
n = 10
d = 3

an = a1 + (n - 1) * d

restulado = suma_serie_aritmetica(a1,an,n)

print(f'La suma de los primero {n} términos es: {restulado}')