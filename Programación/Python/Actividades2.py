import sys
from math import pi,trunc
import random
import statistics
import os
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 54.
os.system ("clear")
print("Actividad 54")
hahaha = True
while hahaha:
    x = input("""--------------------------------------------------------
    Nombre de usuario:
    El nombre de usuario debe tener entre 6 y 12 carácteres.
    Sólo puede ser alfanumérico.
    --------------------------------------------------------
    Escribe:""")
    y = len(x)
    os.system ("clear")
    if y < 6:
        os.system ("clear")
        print("¡ERROR! Su nombre de usuario debe contener al menos 6 carácteres.")
    elif y > 12:
        os.system ("clear")
        print("¡ERROR! Su nombre de usuario no puede contener más de 12 carácteres.")
    else:
        z = x.isalnum()
        if z == False:
            print("¡ERROR! Su nombre de usuario sólo puede ser alfanumérico.")
        else:
            os.system ("clear")
            print("Bienvenido",x)
            hahaha = False
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 55.
os.system ("clear")
print("Actividad 55")
hahaha = True
while hahaha:
    x = input("""--------------------------------------------------------
    Contraseña:
    La contraseña debe tener cómo mínimo 8 carácteres.
    Debe contener letras mayusculas, minusculas, números y al menos 1 carácter no alfanuménico.
    --------------------------------------------------------
    Escribe:""")
    if len(x) < 8:
        os.system("clear")
        print("¡ERROR! La contraseña tiene que contenter al menos 8 carácteres.")
    else:
        s = 0
        my = 0
        mn = 0
        d = 0
        for y in x:
            if y.isspace()==True:
                s += 1
            if y.isupper()==True:
                my += 1
            if y.islower()==True:
                mn += 1
            if y.isdigit()==True:
                d += 1
        if s >= 1:
            os.system("clear")
            print("¡ERROR! La contraseña no puede contener espacios.")
        elif my < 1:
            os.system("clear")
            print("¡ERROR! La contraseña debe contener mayusculas.")
        elif mn < 1:
            os.system("clear")
            print("¡ERROR! La contraseña debe contener minusculas.")
        elif d < 1:
            os.system("clear")
            print("¡ERROR! La contraseña debe contener números.")
        else:
            hahaha = False
os.system("clear")
print("Tu contraseña es",x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 56.
os.system ("clear")
print("Actividad 56")
while True:
    name = input("Escribe un nombre de usuario: ")
    pswd = input("Escribe una contraseña: ")
    cname = len(name)
    cpswd = len(pswd)
    os.system ("clear")
    if cname < 6 or cpswd < 8:
        os.system ("clear")
        if cname < 6:
            print("¡ERROR! Su nombre de usuario debe contener al menos 6 carácteres.")
        elif cpswd < 8:
            print("¡ERROR! La contraseña tiene que contenter al menos 8 carácteres.")
        else:
            print("¡ERROR! Tanto el nombre de usuario como la contraseña tienen menos carácteres de los requeridos")
    elif cname > 12:
        os.system ("clear")
        print("¡ERROR! Su nombre de usuario no puede contener más de 12 carácteres.")
    elif name.isalnum()== False:
        os.system ("clear")
        print("¡ERROR! Su nombre de usuario sólo puede ser alfanumérico.")
    while True:
        s = 0
        my = 0
        mn = 0
        d = 0
        for i in pswd:
            if i.isspace()==True:
                s += 1
            if i.isupper()==True:
                my += 1
            if i.islower()==True:
                mn += 1
            if i.isdigit()==True:
                d += 1
        if s >= 1:
            os.system("clear")
            print("¡ERROR! La contraseña no puede contener espacios.")
            break
        elif my < 1:
            os.system("clear")
            print("¡ERROR! La contraseña debe contener mayusculas.")
            break
        elif mn < 1:
            os.system("clear")
            print("¡ERROR! La contraseña debe contener minusculas.")
            break
        elif d < 1:
            os.system("clear")
            print("¡ERROR! La contraseña debe contener números.")
            break
        else:
            os.system("clear")
            print("Bienvenido",name)
            print("Su contraseña es",pswd)
            break
    else:
        break
    break
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 57.
os.system ("clear")
print("Actividad 57")
#En consola.
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 58.
os.system ("clear")
print("Actividad 58")
#En consola.
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 59.
os.system ("clear")
print("Actividad 59")
x = int(input("Cuantos datos quieres ingresar? "))
y = []
num = 0
for i in range(1,x+1):
    i = float(input(f"Dato {i}:"))
    y.append(i)
    num += i
mid = num/x
c = 0
for i in y:
    if i > mid:
        c += 1
if c == 1:
    print(c,"dato es mayor que el promedio.")
elif c > 1:
    print(c,"datos son mayores que el promedio.")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 60.
os.system ("clear")
print("Actividad 60")
def contar_letras(x):
    d = {}
    x = x.lower()
    for i in x:
        if i.isalnum() == True:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    print(d)
x = input("Escribe una oración: ")
contar_letras(x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 61.
os.system ("clear")
print("Actividad 61")
def contar_iniciales(x):
    d = {}
    x = x.lower()
    x = x.split()
    for i in x:
        i = i[0]
        if i.isalnum() == True:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    print(d)
x = input("Escribe una oración: ")
contar_iniciales(x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 62.
os.system ("clear")
print("Actividad 62")
def contar_largo_palabras(x):
    d = {}
    x = x.lower()
    x = x.split()
    for i in x:
        num = len(i)
        if i.isalnum() == True:
            d[i] = num
    print(d)
x = input("Escribe una oración: ")
contar_largo_palabras(x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 63.
os.system ("clear")
print("Actividad 63")
def mas_larga(x):
    pm = len(x[0])
    ps = x[0]
    for y in x:
        if pm <= len(y):
            ps = y
            pm = len(y)
        else:
            ps = ps
    print(ps)
x = []
while True:
    escr = input("""Escribe una palabra 
                 (cuando escribas 0, dejarás
                 de escribir palabras y te 
                 daré el resultado): """)
    if escr != "0":
        x.append(escr)
    else:
        break
mas_larga(x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 64.
os.system ("clear")
print("Actividad 64")
def filtrar_palabras(x,y):
    z = []
    for w in x:
        if len(w) >= y:
            z.append(w)
    if len(z) == 0:
        print("No hay palabras...")
    else: 
        print(z)
x = []
while True:
    escr = input("""Escribe una palabra 
                 (cuando escribas 0, dejarás
                 de escribir palabras y te 
                 daré el resultado): """)
    if escr != "0":
        x.append(escr)
    else:
        y = int(input("Dime un número:"))
        break
filtrar_palabras(x,y)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 65.
os.system ("clear")
print("Actividad 65")
x = input("Escribe una oración:")
c = 0
for i in list(x):
    if i.isupper() == True:
        c += 1
    else:
        c += 0
print("En tu oración hay",c,"mayusculas.")
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 66.
os.system ("clear")
print("Actividad 66")
def bin_dec(x):
    bd = int(str(x), 2)
    print("El numero que has escrito es: ",bd)
x = int(input("Escribe un número binario:"))
bin_dec(x)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 67.
os.system ("clear")
print("Actividad 67:")
x = int(input("Escribe el año actual: "))
y = []
for xd in [0,3]:
    z = int(input(f"Escribe el nombre {xd} : "))
    y.append(z)
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 67.
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 68.
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 69.
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 70.
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 71.
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 72.
#----------------------------------------------------------------------------------------------------------------------------------
#Actividad 73.
