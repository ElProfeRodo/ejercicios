'''
2. Crear una función que solicite la edad por el teclado, y muestre por pantalla si el
usuario es mayor o menor de edad
'''
def mayor_edad():
    edad = int(input("ingrese su edad: "))
    if edad >= 18:
        return "usted es mayor de edad"
    else:
        return "usted es menor de edad"

print('verificaion de edad:',mayor_edad())
