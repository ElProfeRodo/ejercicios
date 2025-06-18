# 5. Sumar los números impares dentro de un rango dado
def sumar_impares(minimo, maximo):
    suma = 0
    numero = int(minimo)
    final = int(maximo)
    while numero <= final:
        if numero % 2 != 0:
            suma = suma + numero
        numero = numero + 1
    return suma

minimo = input("Ingrese el número mínimo del rango: ")
maximo = input("Ingrese el número máximo del rango: ")
print("Ejercicio 5 - Suma de impares entre el rango:", sumar_impares(minimo, maximo))
