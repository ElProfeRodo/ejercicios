# 6. Suma, resta, multiplicación y división segura
def operaciones_basicas(a, b):
    a = int(a)
    b = int(b)
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division = "No se puede dividir por cero"
    else:
        division = a / b
    return suma, resta, multiplicacion, division

a = input("Ingrese el primer número: ")
b = input("Ingrese el segundo número: ")
s, r, m, d = operaciones_basicas(a, b)
print("Ejercicio 6 - Operaciones básicas:")
print("  Suma:", s)
print("  Resta:", r)
print("  Multiplicación:", m)
print("  División:", d)

