import sys
from math import pi,trunc
import random
import statistics
import os
#Actividad 63.
os.system ("clear")
print("Actividad 63")
def mas_larga(x):
    z = []
    max = z[0]
    x = x.lower()
    x = x.split()
    for i in x:
        if i.isalnum() == True:
            num = len(i)
            z.append(num)
    for i in z:
        if i > max:
            max = i
    return max
    print(max)
x = input("Escribe una oración: ")
mas_larga(x)