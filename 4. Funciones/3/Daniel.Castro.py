# 3. Crear correo electrónico con nombre/apellido
def generar_correo(nombre, apellido):
    correo = nombre + "." + apellido + "@gmail.com"
    return correo

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print("Ejercicio 3 - Correo generado:", generar_correo(nombre, apellido))
