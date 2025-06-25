"""
5. Dada la lista animales = [“perro”, “gato”, “pájaro”, “pez”], elimina
“gato” y muestra por pantalla el resultado.
"""
animales = ["perro", "gato", "pajaro", "pez"]
for a in animales:
    print("1:")
    print(a)

animales.remove("gato")
for a in animales:
    print("2:")
    print(a)