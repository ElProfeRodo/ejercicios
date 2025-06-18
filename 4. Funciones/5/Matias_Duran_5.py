def suma_impares_rango(inicio, fin):
    suma = 0
    for i in range(inicio, fin + 1):
        if i % 2 != 0:
            suma += i
    return suma

resultado = suma_impares_rango(3, 8)
print(f"La suma de los numeros impares en el rango es {resultado}")
    
    
