def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == "".join(reversed(palabra))

palabra = input("Ingrese una palabra: ")

if palindromo(palabra):
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")
