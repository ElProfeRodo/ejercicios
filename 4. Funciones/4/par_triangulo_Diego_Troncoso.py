"""
Crear una función que reciba como parámetro la altura y el ancho de un rectángulo
(en centímetros) para calcular su área. El resultado debe mostrarse por pantalla.
"""
def area_rectangulo():
    altura= int(input("Igrese la altura del cuadrado: "))
    ancho= int(input("Ingrese el ancho del cuadrado: "))
    
    area= altura * ancho
    return area
resultado= area_rectangulo()
print("El area de rectangulo es: ", resultado)