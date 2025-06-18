#ejercicio4

def rec_area(altura, ancho):
    area = altura * ancho
    return area

al = float(input('Ingrese el largo: '))
an = float(input('Ingrese el ancho: '))

print(f'su area es: {round(rec_area(al,an))}')
