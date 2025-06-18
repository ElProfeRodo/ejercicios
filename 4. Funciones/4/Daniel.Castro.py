# 4. Calcular el área de un rectángulo
def calcular_area_rectangulo(altura, ancho):
    area = int(altura) * int(ancho)
    return area

altura = input("Ingrese la altura del rectángulo: ")
ancho = input("Ingrese el ancho del rectángulo: ")
print("Ejercicio 4 - Área del rectángulo:", calcular_area_rectangulo(altura, ancho), "cm cuadrados")
