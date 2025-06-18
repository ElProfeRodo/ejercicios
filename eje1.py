def suma():
    numeros=[]
    for i in range(15):
        num=int(input("ingrese un numero: "))
        numeros.append(num)
    suma=sum(numeros)
    print(f"la suma de los numeros es:{suma} ")
suma()