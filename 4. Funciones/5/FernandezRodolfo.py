def suma_impares(min, max):
    suma = 0
    for i in range(min, max+1):
        if i % 2 != 0:
            suma += i
    return suma

suma_impares(8, 14)