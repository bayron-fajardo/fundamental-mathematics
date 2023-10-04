def interes_compuesto(p,r,n,t):
    #Formula de interes compuesto
    A = round((p*(1+(r/n))**(n*t)),2)
    return A

#Datos
p = 1000
r = 0.05
n = 1
t = 5

resultado = interes_compuesto(p,r,n,t)
print(resultado)