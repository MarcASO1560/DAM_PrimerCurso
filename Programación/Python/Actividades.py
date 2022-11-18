import sys
from math import pi,trunc
import random
import statistics
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 1:
print("Actividad 1:")
print("La versión actual de python es:",sys.version)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 2:
print("Actividad 2:")
print(
"\nTwinkle, twinkle, little star,\t", "\n\tHow I wonder what you are!", "\n\t\tUp above the world so high", "\n\t\tLike a diamond in the sky.","\nTwinkle, twinkle, little star,\t","\n\tHow I wonder what you are"
)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 3:
print("Actividad 3:")
x=input("Insterta tu nombre:")
print("Tu nombre es:",x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 4:
print("Actividad 4:")
n=input("Cual es su edad:")
print("El número elegido es:", int(n))
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 5:
print("Actividad 5:")
r=float(input("Radio de la circumferencia:"))
A = pi * r * r
print("La area del circulo equivale a:",A)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 6:
print("Actividad 6:")
lname = input("Introduzca sus apellidos:")
fname = input("Introduzca su nombre:")
print("Su nombre completo es:",fname + " " + lname)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 7:
print("Actividad 7:")
N1 = int(input("Primera nota:"))
N2 = int(input("Segunda nota:"))
N3 = int(input("Tercera nota:"))
N4 = int(input("Cuarta nota:"))
Ntotal = (N1 + N2 + N3 + N4) / 4
print("El promedio es:",Ntotal)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 8:
print("Actividad 8:")
Texto = input("Escribe un texto:")
numT = len(Texto)
print("El texto que has escrita contiene",numT, "carácteres.")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 9:
print("Actividad 9:")
c1 = int(input("Primera nota:"))
c2 = int(input("Segunda nota:"))
nl = int(input("Nota de laboratorio:"))
nf = 60
c3 = (3*(nf-nl*0.3)/0.7)-c2-c1
nc = (c1+c2+c3)/3
print("Necesitas una nota de",round(c3),"en el examen 3")
#----------------------------------------------------------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 11:
print("Actividad 11:")
salbr = float(input("Introduzca su salario en bruto (€):"))
ts1 = salbr - ((salbr / 100) * 5)
ts2 = salbr - ((salbr / 100) * 10)
ts3 = salbr - ((salbr / 100) * 12)
if salbr < 1000.00:
    print("Tu impuesto será del 0% por lo tanto su salario neto será de",round(salbr,2),"€")
elif salbr >= 1000.00 and salbr < 2000.00:
    print("Tu impuesto será del 5% por lo tanto su salario neto será de",round(ts1,2),"€")
elif salbr >= 2000.00 and salbr < 4000.00:
    print("Tu impuesto será del 10% por lo tanto su salario neto será de",round(ts2,2),"€")
elif salbr >= 4000.00:
    print("Tu impuesto será del 12% por lo tanto su salario neto será de",round(ts3,2),"€")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 12:
print("Actividad 12:")
x = int(input("Introduzca un numero:"))
if x < 10:
    print("El numero",x,"es menor que 10.")
elif x > 10:
    print("El numero",x,"es mayor que 10.")
else:
    print("El numero",x,"es igual que 10.")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 13:
print("Actividad 13:")
x = int(input("Introduzca un numero:"))
n = x % 2
if n == 0:
    print("El numero",x,"es par.")
else:
    print("El numero",x,"es impar.")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 14:
print("Actividad 14:")
x = 0
y = 10
w = 1
while x <= y:
    print(x)
    x += w
#----------------------------------------------------------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------------------------------------------
#Activitat 17:
print("Activitat 17:")
x = int(input("Introduzca un numero:"))
y = int(input("Introduzca otro numero:"))
if x > y:
    print("Menor:",x,">","Mayor:",y)
elif x < y:
    print("Menor:",y,">","Mayor:",x)
elif x == y:
    print(x,"=",y)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 18:
print("Actividad 18:")
x = int(input("Introduzca un numero:"))
y = int(input("Introduzca otro numero:"))
mul = 0
div = 0
if y == 0:
    print("La división entre",x,"y",y,"no es posible.")
elif x and y > 0:
    if x == 0:
        print("El resultado de una división de 0 entre cualquier número, siempre es 0.")
        print("Por lo tanto es múltiple.")
    elif x >= y:
        mul = x % y
        div = x / y
        if mul == 0:
            print(float(div))
            print(x,"és múltiple de",y)
        else:
            print(float(div))
            print(x,"no és múltiple de",y)
    elif y >= x:
        mul = y % x
        div = y / x
        if mul == 0:
            print(float(div))
            print(y,"és múltiple de",x)
        else:
            print(float(div))
            print(y,"no és múltiple de",x)
else:
    if x == 0:
        print("El resultado de una división de 0 entre cualquier número, siempre es 0.")
        print("Por lo tanto es múltiple.")
    elif x >= y:
        mul = y % x
        div = y / x
        if mul == 0:
            print(float(div))
            print(x,"és múltiple de",y)
        else:
            print(float(div))
            print(x,"no és múltiple de",y)
    elif y >= x:
        mul = x % y
        div = x / y
        if mul == 0:
            print(float(div))
            print(y,"és múltiple de",x)
        else:
            print(float(div))
            print(y,"no és múltiple de",x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 19:
print("Actividad 19:")
x = int(input("Introduzca el primer número:"))
y = int(input("Introduzca el segundo número:"))
w = int(input("Introduzca el tercer número:"))
if x == y and x == w:
    print("Los 3 números son iguales.")
elif x == y:
    print(x,"y",y,"son iguales.")
elif x == w:
    print(x,"y",w,"son iguales.")
elif y == w:
    print(y,"y",w,"son iguales.")
else:
    print("Los 3 números son distintos.")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 20:
print("Actividad 20:")
x = int(input("Introduce un año y te diré si es biciesto o no:"))
calc = x % 4
if calc == 0:
    print("El año",x,"es un número biciesto porque es multiple de 4.")
else:
    print("El año",x,"no es un número biciesto.")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 21:
print("Actividad 21:")
x = input(
"""-------------------------------------------
Escoje una figura geometrica para calcular su area: 
-Triangulo (T)
-Circulo (C)
-------------------------------------------
Elige 'C' o 'T': """)
if x == "C":
    r = float(input("Introduce el radio del circulo:"))
    a = pi * r**2
    print("La area del circulo es:",a)
elif x == "T":
    b = float(input("Introduce la base del triangulo:"))
    alt =  float(input("Introduce la altura del triangulo:"))
    a = (b * alt) / 2
    print("La area del triangulo es:",float(a,2))
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 22:
print("Actividad 22:")
cm = float(input("Introduce la cantidad de centímetros:"))
if cm < 100:
    print("Tu distancia es",cm,"centímetros:")
elif cm >= 100 and cm < 100000:
    m = cm / 100
    cm1 = m - trunc(m)
    print("Tu distancia es",trunc(m),"metros y",round(cm1*100),"centímetros.")
elif cm >= 100000:
    km = cm / 100000
    m1 = (km - trunc(km))*1000
    cm2 = (m1 - trunc(m1))*100
    print("Tu distancia es",trunc(km),"kilómetros",round(m1),"metros y",round(cm2),"centímetros.")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 23:
print("Actividad 23:")
x = float(input("Escribe un número, cuando escribas el número 0, saldrá del bucle:"))
y = [x]
while x != 0:
    x = float(input("Escribe otro número:"))
    if x == 0:
        print("Los números que has escrito són:",y)
        break
    else:
        y.append(x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 24:
print("Activiad 24:")
x = float(input("Escribe una nota entre 0 y 10:"))
y = [x]
while x >= 0 or x <= 10:
    x = float(input("Escribe otra nota:"))
    if x < 0 or x > 10:
        print("Las notas que has escrito son:",y)
        break
    else:
        y.append(x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 25:
print("Actividad 25:")
x1 = float(input("Introduce un número:"))
x2 = 0
y = [x1]
while x1 >= x2:
    x2 = x1
    x1 = float(input("Escribe otro número mayor que el anterior:"))
    if x1 < x2:
        print("Los números escritos son:",y)
    else:
        y.append(x1)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 26:
print("Actividad 26:")
while True:
    min = float(input("Introduce un número:"))
    max = float(input("Introduce un número mayor que el anterior:"))
    y = []
    if min > max:
        print(min,"es mayor que",max,"Por lo tanto vuelve a empezar.")
    else:
        x = float(input("Elige un número que esté entre el minimo y el maximo elegidos:"))
        while True:
            if x >= min and x <= max:
                y.append(x)
                x = float(input("Elige otro número que esté entre el minimo y el maximo elegidos:"))
            else:
                break
        print("Los números situados entre",min,"y",max,"son:",y)
        break
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 27:
print("Actividad 27:")
lim = float(input("Introduce un número límite:"))
y = []
while True:
    z = 0
    while True:
        x = float(input("Escribe un valor menor al límite:"))
        if z >= lim:
            print("El limite a superar es",lim,". La lista creada es:",y)
            break
        elif z < lim:
            y.append(x)
            z += x
    break
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 28:
print("Actividad 28:")
while True:
    min = int(input("Introduce un número mínimo:"))
    max = int(input("Introduce un número máximo:"))
    if min > max:
        print(min,"es mayor que",max,"Por lo tanto vuelve a empezar.")
    if max >= min:
        x = random.randrange(min,max)
        c = 0
        print("Empieza el juego. Adivina el numero randomizado entre",min,"y",max,":")
        while True:
            y = float(input("Introduce un número:"))
            if y < x:
                print("¡Demasiado pequeño!")
                c += 1
            elif y > x:
                print("¡Demasiado grande!")
                c += 1
            else:
                if c == 0:
                    print("¡Acertaste a la primera!")
                    break
                else:
                    print("¡Acertaste! Te ha costado",c,"intentos.")
                    break
        break
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 29:
print("Actividad 29:")
x = list(range(0,10))
print(x)
x = list(range(4,11))
print(x)
x = list(range(-6,1))
print(x)
x = list(range(-56,-49))
print(x)
x = list(range(1,18,2))
print(x)             
x = list(range(-6,11,2))
print(x)
x = list(range(100,1001,100))
print(x)
x = list(range(10,3,-1))
print(x)
x = list(range(-50,-57,-1))
print(x)
x = list(range(17,0,-2))
print(x)
x = list(range(1000,99,-100))
print(x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 30:
print("Actividad 30:")
while True:
    x = float(input("Introduce un número positivo:"))
    if x < 0:
        print(x,"no es un número positivo:")
    else:
        y = list(range(0,int(x + 1),1))
        print(y)
        y = list(range(int(x),-1,-1))
        print(y) 
        y = list(range(1,int(x),1))
        print(y)
        y = list(range(int(x - 1),0,-1))
        print(y)
        y = list(range(0,int(x + 1),1)) + list(range(int(x - 1),-1,-1))
        print(y)
        break
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 31:
print("Actividad 31:")
x = float(input("Introduce un número:"))
if x > 0:
    y = list(range(0,int(x+1),1))
    print("El resultado es:",y)
elif x < 0:
    y = list(range(0,int(x-1),-1))
    print("El resultado es:",y)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 32:
print("Actividad 32:")
while True:
    min = float(input("Introduce el primer número:"))
    max = float(input("Introduce un número mayor que el primero:"))
    if min > max:
        print(min,"es mayor que",max,". Por lo tanto vuelve a empezar.")
    else:
        y = list(range(int(min),int(max + 1),1))
        print(y)
        y = list(range(int(max - 1),int(min - 1),-1))
        print(y)
        y = list(range(int(min + 1),int(max + 2),1))
        print(y)
        y = list(range(int(max - 1),int(min),-1))
        print(y)
        y = list(range(int(min),int(max + 1),1)) + list(range(int(max - 1),int(min - 1),-1))
        print(y)
        break
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 33:
print("Actividad 33:")
x = float(input("Escribe un número inicial:"))
y = float(input("Escribe un número final:"))
if x > y:
    w = list(range(int(y),int(x),-1))
    print(w)
if x < y:
    w = list(range(int(x),int(y),1))
    print(w)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 34:
print("Actividad 34:")
x = float(input("Escribe un número inicial:"))
y = float(input("Escribe un número final:"))
if x > y:
    w = list(range(int(y + 1),int(x),1))
    print(w)
if x < y:
    w = list(range(int(x + 1),int(y),1))
    print(w)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 35:
print("Actividad 35:")
x = float(input("Introduce un valor inicial:"))
y = float(input("Introduce cuantos valores quieres:"))
z = x + y
w = list(range(int(x),int(z),1))
print(w)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 36:
print("Actividad 36:")
x = float(input("Introduce un valor:"))
y = float(input("Introduce otro valor:"))
if x%2==0 or y%2==0:
    if x%2==0 and y%2==0:
        z = list(range(int(x),int(y+1),2))
        print(z)
    elif x%2==0:
        z = list(range(int(x),int(y),2))
        print(z)
    else:
        z = list(range(int(x+1),int(y+1),2))
        print(z)
else:
    z = list(range(int(x+1),int(y),2))
    print(z)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 37:
print("Actividad 37:")
x = float(input("Dime el valor inicial:"))
y = float(input("Dime el valor final:"))
z = float(input("De que valor quieres los múltiplos:"))
c = x
while True:
    if x%z == 0:
        w = list(range(int(x),int(y),int(z)))
        c = len(w)
        print(w)
        print("Entre",int(c),"y",int(y),"hay",c,"múltiplos de",int(z),".")
        break
    elif x%z != 0:
        if x>y:
            print("ni",c,"ni ningún valor entre este y",y, "es múltiplo de",z)
            break
        else:
            x+=1
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 38:
print("Actividad 38:")
x = int(input("Escribe un numero:"))
y = int(input("Escribe un numero mayor al anteriór:"))
z = list(range(x,y + 1))
w = 0
c = []
for i in z:
    w += i
    c.append(i)
print("La suma de",c,"es",w)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 39:
print("Actividad 39:")
x = int(input("Introduce cuántos valores quieres escribir:"))
c = 0
for i in range(5):
    y = int(input(f"Introduce el valor {i+1}:"))
    c += y
print("La suma es",c)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 40:
print("Actividad 40:")
x = int(input("Introduce la cantidad de valores que quieres escribir:"))
c = 0
for i in range(x):
    y = int(input(f"Introduce el número {i+1}:"))
    if y < 0:
        c += 1
    else:
        c += 0
print("Has escrito",c,"valores negativos:")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 41:
print("Actividad 41:")
x = int(input("Introduce la cantidad de valores que quieres escribir:"))
c = 0
w = []
for i in range(x):
    y = int(input(f"Introduce el número {i+1}:"))
    w.append(y)
wm1 = min(w)
wm2 = max(w)
wm3 = statistics.mean(w)
print("El valro más pequeno es:",wm1)
print("El valro más grande es:",wm2)
print("La media de los numeros es:",wm3)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 42:
print("Actividad 42:")
x = int(input("Introduce la anchura del rectángulo: "))
y = int(input("Introduce la altura del rectángulo: "))
for i in range(y):
    print("*"*x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 43:
print("Actividad 43:")
x = int(input("Introduce la altura del rectángulo: "))
for i in range(x+1):
    print("*"*i)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 44:
print("Actividad 44:")
x = int(input("Introduce la altura del rectángulo: "))
for i in range(x):
    print("*"*i)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 45:
print("Actividad 45:")
x = int(input("Introduce la altura del rectángulo: "))
for i in range(x):
    print("*"*i)
for i in range(x,0,-1):
    print("*"*i)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 46:
print("Actividad 46:")
x = int(input("Introduce la altura del árbol: "))
x = x*2
y = x - 1
for i in range(1,x,2):
        y -= 1
        print(" " * y,"*" * i)
for i in range(x-6,x+5,2):
        y -= 1
        print(" " * (y+3),"*" * i)
for i1 in range(2):
        print(" "*(x-3),"|"*3)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 47:
print("Actividad 47:")
x = int(input("EScribe los valores sin la letra de un DNI:"))
c = x%23
y = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
print("La letra de tu DNI es: ", y[c])
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 48:
print("Actividad 48:")
x = float(input("Introduce una cantidad de euros(sin el símbolo por favor xd):"))
d = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
y = []
for i in d:
	while True:
		if i <= x:
			y.append(i)
			x -= i
		else:
			break
for u in d:
	yc = y.count(u)
	if yc != 0:
		if u >= 5:
			if yc == 1:
				print(yc,"billete de",u,"€")
			else:
				print(yc,"billetes de",u,"€")
		else:
			if yc == 1:
				print(yc,"moneda de",u,"€")
			else:
				print(yc,"monedas de",u,"€")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 49:
print("Actividad 49:")
a,e,i,o,u = "aA","eE","iI","oO","uU"
chain = (input("Escribe un texto y te diré cuantas y cuáles vocales hay:"))
ct,ca,ce,ci,co,cu = 0,0,0,0,0,0
for y in chain:
	if y in a:
		ct += 1
		ca += 1
	if y in e:
		ct += 1
		ce += 1
	if y in i:
		ct += 1
		ci += 1
	if y in o:
		ct += 1
		co += 1
	if y in u:
		ct += 1
		cu += 1
print("Cantidad de (a,A):",ca)
print("Cantidad de (e,E):",ce)
print("Cantidad de (i,I):",ci)
print("Cantidad de (o,O):",co)
print("Cantidad de (u,U):",cu)
print("Cantidad de vocales en total:",ct)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 50:
print("Actividad 50:")
v = "aáàAÁÀeéèEÉÈiíìïIÍÌÏoóòOÓÒuúùüUÚÙÜ"
chain = (input("Escribe un texto y te borraré las vocales:"))
for y in range(len(v)):
		chain = chain.replace(v[y],"")
print(chain)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 51:
print("Actividad 51:")
chain = (input("Escribe un texto y te contaré las palabras:"))
x = chain.split()
y = len(x)
if y == 1:
	print("Tu texto tiene 1 palabra.")
elif y > 1:
	print("Tu texto tiene",y,"palabras.")








