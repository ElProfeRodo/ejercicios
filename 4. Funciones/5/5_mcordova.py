def rangos(min,max):
    suma = 0
    for numero in range(min,max):
        if numero % 2 != 0:
            suma = suma + numero
    return suma
    
min = int(input('Ingrese el mínimo: '))
max = int(input('Ingrese el máximo: '))

print(rangos(min,max))
