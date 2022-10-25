#Actividad 26:
print("Actividad 26:")
while True:
    min = float(input("Introduce un número:"))
    max = float(input("Introduce un número anterior que el anterior:"))
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