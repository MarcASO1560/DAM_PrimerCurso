import sys
from math import pi
#Actividad 1:
print("Actividad 1:")
print("La versión actual de python es:",sys.version)
#Actividad 2:
print("Actividad 2:")
print(
"\nTwinkle, twinkle, little star,\t", "\n\tHow I wonder what you are!", "\n\t\tUp above the world so high", "\n\t\tLike a diamond in the sky.","\nTwinkle, twinkle, little star,\t","\n\tHow I wonder what you are"
)
#Actividad 3:
print("Actividad 3:")
x=input("Insterta tu nombre:")
print("Tu nombre es:",x)
#Actividad 4:
print("Actividad 4:")
n=input("Cual es su edad:")
print("Tu edad es:", int(n))
#Actividad 5:
print("Actividad 5:")
r=float(input("Radio de la circumferencia:"))
A = pi * r * r
print("La area del circulo equivale a:",A)
#Actividad 6:
print("Actividad 6:")
lname = input("Introduzca sus apellidos:")
fname = input("Introduzca su nombre:")
print("Su nombre completo es:",fname + " " + lname)
#Actividad 7:
print("Actividad 7:")
N1 = float(input("Primera nota:"))
N2 = float(input("Segunda nota:"))
N3 = float(input("Tercera nota:"))
N4 = float(input("Cuarta nota:"))
Ntotal = round((N1 + N2 + N3 + N4) / 4)
print("El promedio es:",Ntotal)
#Actividad 8:
print("Actividad 8:")
Texto = input("Escribe un texto:")
numT = len(Texto)
print("El texto que has escrita contiene",numT, "carácteres.")
#Actividad 9:
print("Actividad 9:")
c1 = float(input("Primera nota:"))
c2 = float(input("Segunda nota:"))
nl = int(input("Nota de laboratorio:"))
nf = 60
c3 = (3*(nf-nl*0.3)/0.7)-c2-c1
nc = (c1+c2+c3)/3
print("Necesitas una nota de",round(c3),"en el examen 3")
#Actividad 10:
print("Actividad 10:")
pc = float(input("Introduce tu peso corporal (Kg):"))
alt = float(input("Introduce tu altura (m):"))
imc = pc / alt**2
print("Tu índice de masa corporal es:",round(imc))
if imc < 16.00:
    print("Tienes un problema serio.")
elif imc >= 16.00 and imc <= 17.00:
    print("Estas muy flaco, cuidate.")
elif imc > 17.00 and imc <= 18.50:
    print("Estas delgado, pero no pasa nada.")
elif imc > 18.50 and imc <= 25.00:
    print("Tas bien.")
elif imc > 25.00 and imc <= 30.00:
    print("A ver... No pasa nada pero cuidado.")
elif imc > 30.00 and imc <= 35.00:
    print("Uff... preocupa un poco.")
elif imc > 35.00 and imc <= 40.00:
    print("Si eres capaz de mantenerte en pié, te aplaudo.")
elif imc >= 40.00:
    print("Trata de rodar como en Dark Souls.")
#Actividad 11:
print("Actividad 11:")
salbr = float(input("Introduzca su salario en bruto (?):"))
ts1 = salbr - ((salbr / 100) * 5)
ts2 = salbr - ((salbr / 100) * 10)
ts3 = salbr - ((salbr / 100) * 12)
if salbr < 1000.00:
    print("Tu impuesto será del 0% por lo tanto su salario neto será de",round(salbr,2),"?")
elif salbr >= 1000.00 and salbr < 2000.00:
    print("Tu impuesto será del 5% por lo tanto su salario neto será de",round(ts1,2),"?")
elif salbr >= 2000.00 and salbr < 4000.00:
    print("Tu impuesto será del 10% por lo tanto su salario neto será de",round(ts2,2),"?")
elif salbr >= 4000.00:
    print("Tu impuesto será del 12% por lo tanto su salario neto será de",round(ts3,2),"?")
#Actividad 12:
print("Actividad 12:")
x = int(input("Introduzca un numero:"))
if x < 10:
    print("El numero",x,"es menor que 10.")
elif x > 10:
    print("El numero",x,"es mayor que 10.")
else:
    print("El numero",x,"es igual que 10.")
#Actividad 13:
print("Actividad 13:")
x = int(input("Introduzca un numero:"))
n = x % 2
if n == 0:
    print("El numero",x,"es par.")
else:
    print("El numero",x,"es impar.")
#Actividad 14:
print("Actividad 14:")
x = 0
y = 10
w = 1
while x <= y:
    print(x)
    x += w
#Actividad 15:
print("Actividad 15:")
pa = int(input("Introduzca el primer año:"))
sa = int(input("Introduuzca el segundo año:"))
x = 0
if sa > pa:
    x = sa - pa
    print("Del año",pa,"hasta el año",sa,"pasaran",x,"años.")
elif pa > sa:
    x = pa - sa
    print("Del año",sa,"hasta el año",pa,"pasaran",x,"años.")
else:
    print("Los dos años son iguales...")
#Actividad 16:
print("Actividad 16:")
x = int(input("Introduzca un numero:"))
y = int(input("Introduzca otro numero:"))
res = 0
div = 0
if x > y:
    div = x / y
    res = x % y
    if res == 0:
        print("La división es exacta, el resultado entre",x,"y",y,"es",round(div),"y el resto es",res,".")
    else:
        print("La división no es exacta, el resultado entre",x,"y",y,"es",round(div),"y el resto es",res,".")
elif x < y:
    div = y / x
    res = y % x
    if res == 0:
        print("La división es exacta, el resultado entre",y,"y",x,"es",round(div),"y el resto es",res,".")
    else:
        print("La división no es exacta, el resultado entre",y,"y",x,"es",round(div),"y el resto es",res,".")
#Activitat 17:
print("Activitat 17:")
x = int(input("Introduzca un numero:"))
y = int(input("Introduzca otro numero:"))
if x > y:
    print(x,">",y)
elif x < y:
    print(y,">",x)
elif x == y:
    print(x,"=",y)

