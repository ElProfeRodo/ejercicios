'''
7. Crear un programa que determine si una palabra es un palíndromo.
'''
def es_palindromo(palabra):
    palabra_limpia = palabra.replace(" ", "").lower()
    return palabra_limpia == palabra_limpia[::-1]

palabra = input("Ingresa una palabra: ")

if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')
