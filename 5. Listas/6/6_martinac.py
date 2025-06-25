n = int(input('Ingrese la cantidad de numeros pares que desee: '))
lista = []
for i in range(1,n):
    if i % 2 == 0: 
        lista.append(i)
print(lista)