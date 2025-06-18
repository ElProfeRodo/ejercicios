"""
1. Crear una función que solicite 15 números por el teclado, y muestre por pantalla la
suma de ellos.
"""
def sumatoria():
    suma = 0
    contador = 1
    while contador<= 15:
        numero= input("Ingrese un número: ")
        suma = suma+ int(numero)
        contador+= 1
    return suma

print("La suma de 15 números es:",sumatoria())
