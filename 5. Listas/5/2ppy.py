def suma_impares(minimo, maximo):
    suma = 0
    for numero in range(minimo, maximo + 1):
        if numero %2 != 0:
            suma += numero
        return suma
    
minimo = int(input("ingresa el valor minimo: "))
maximo = int(input("ingresa el valor maximo: "))

resultado = suma_impares(minimo, maximo)
print("la suma de ambos numeros impares es: ")