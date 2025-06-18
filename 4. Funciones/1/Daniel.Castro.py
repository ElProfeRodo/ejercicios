# 1. Sumar 15 números ingresados
def sumar_quince_numeros():
    suma= 0
    contador= 1
    while contador<= 15:
        numero= input("Ingrese un número: ")
        suma= suma+ int(numero)
        contador+= 1
    return suma

print("La suma de 15 números:", sumar_quince_numeros())
