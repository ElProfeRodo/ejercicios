# 7. Validar si el nombre de una mascota tiene más de 6 caracteres (2 funciones)
def nombre_mascota_valido(nombre):
    contador = 0
    for letra in nombre:
        contador = contador + 1
    if contador > 6:
        return True
    else:
        return False

def solicitar_y_validar_nombre_mascota():
    nombre = input("Ingrese el nombre de su mascota: ")
    if nombre_mascota_valido(nombre):
        return "El nombre tiene más de 6 caracteres."
    else:
        return "El nombre tiene 6 caracteres o menos."

print("Ejercicio 7 - Validación nombre mascota:", solicitar_y_validar_nombre_mascota())
