def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == "".join(reversed(palabra))

palabra_palindromo = input("Ingrese una palabra: ")

if es_palindromo(palabra_palindromo):
    print(f"{palabra_palindromo} es un palíndromo")
else:
    print(f"{palabra_palindromo} no es un palíndromo")
