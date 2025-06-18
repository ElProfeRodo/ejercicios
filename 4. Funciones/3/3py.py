def crear_email(nombre, apellido):
email = f"{nombre.lower()}.{apellido.lower()}@gamil.com"
return email

nombre = input("ingresar nombre: ")
apellido = input("ingresar apellido: ")

resultado_email = crear_email(nombre, apellido)
print("la direccion de correo electronico es: ,resultado_email")