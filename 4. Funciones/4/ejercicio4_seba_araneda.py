'''
4. Crear una función que reciba como parámetro la altura y el ancho de un rectángulo
(en centímetros) para calcular su área. El resultado debe mostrarse por pantalla.
'''
def calculo_area(altura, ancho):
    area = ancho * altura
    return area

altura = int(input("Ingrese la altura del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))
print(calculo_area(altura, ancho))
