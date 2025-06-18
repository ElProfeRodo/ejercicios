def numeros (minimo,maximo):
    Sumatoria=0
    Num= int(minimo)
    Extremo=int(maximo)
    while Num<=Extremo:
        if Num %2 !=0:
            Sumatoria=Sumatoria+Num
        Num=Num+1
    return Sumatoria

minimo = int(input("Ingresar el numero mas bajo: "))
maximo = int(input("Ingresar el numero mas alto: "))
print(numeros(minimo,maximo))