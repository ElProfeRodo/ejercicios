"""
Crear una función que reciba como parámetro dos números, y retorne la suma,
resta, multiplicación y división de ellos. Debe considerar que la división por cero no
existe
"""
def calculadora(suma, resta, multiplicacion, division):
    primernumero= int(input("Ingrese primer numero: "))
    segundonumero= int(input("Ingresa el segundo numero: "))
    
    suma= primernumero + segundonumero
    resta= primernumero - segundonumero
    multiplicacion= primernumero * segundonumero
    division= primernumero / segundonumero
    
    print(f"La suma de los dos numeros es: {suma}")
    print(f"La resta de los dos numeros es: {resta}")
    print(f"La multiplicacion de los dos numeros es: {multiplicacion}")
    try:
        print(f"La division de los dos numeros es: {division}")
    except ValueError:
        print("La division ingresada no es divisible / division en 0")
        
    return suma, resta, multiplicacion, division
calculo= calculadora(suma=resta=multiplicacion=division=)
print(calculo)
