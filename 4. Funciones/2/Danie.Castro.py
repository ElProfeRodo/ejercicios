# 2. Verificar mayoría de edad
def verificar_mayoria_edad():
    edad= input("Ingrese su edad: ")
    edad= int(edad)
    if edad>= 18:
        return "Es mayor de edad."
    else:
        return "Es menor de edad."

print("Verificación de edad:", verificar_mayoria_edad())

