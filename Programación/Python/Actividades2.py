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

