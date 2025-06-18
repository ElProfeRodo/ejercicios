'''
5. Crear una función que reciba como parámetro dos números, correspondientes al
valor mínimo y máximo de un rango. La función debe retornar la suma de los
números impares dentro de ese rango.
'''
def sumatoria_impares(min,max):
    suma = 0
    for num in range(min,max): 
        if num % 2 != 0: 
            suma = suma + num
    return suma

min = int(input("ingrese un numero Minimo: "))
max = int(input('ingrese un numero Maximo: '))

print(sumatoria_impares())
