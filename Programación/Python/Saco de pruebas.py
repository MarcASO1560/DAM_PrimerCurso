import sys
from math import pi,trunc
import random
import statistics

#Actividad 48:
print("Actividad 48:")
x = float(input("Introduce una cantidad de euros(sin el símbolo por favor xd):"))
bill500 = 500
bill200 = 200
bill100 = 100
bill50 = 50
bill20 = 20
bill10 = 10
bill5 = 5
mon2 = 2
mon1 = 1
mon05 = 0.50
mon02 = 0.20
mon01 = 0.10
mon005 = 0.05
mon002 = 0.02
mon001 = 0.01
y = []
while True:
	if bill500 < x:
		y.append(bill500)
		x -= bill500

	elif bill200 < x:
		y.append(bill200)
		x -= bill200
	elif bill100 < x:
		y.append(bill100)


