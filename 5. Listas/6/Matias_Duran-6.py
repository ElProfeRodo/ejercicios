n = int(input("Ingrese la cantidad de numeros a generar: "))
numeros_pares = []
for i in range(n):
    numeros_pares.append((i + 1) * 2)

print("Los primeros", n, "números pares son:", numeros_pares)
