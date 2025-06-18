"""
Crear una función que solicite 15 números por el teclado, y muestre por pantalla la suma de ellos.
"""

def sumatoria():
    contador = 0
    suma = 0
    while contador < 15:
        contador += 1
        numero = int(input(f"Ingresa numero {contador}: "))
        suma = suma + numero
    print(f"La sumatoria es: {suma}")

sumatoria()