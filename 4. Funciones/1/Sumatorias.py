def suma():
    sumando=0
    contador=0
    while contador<15:
        contador+=1
        numero=int(input(f"{contador}. Ingresar numero: "))
        sumando=sumando+numero
        if contador==15:
            print(f"la suma total de las variantes es: {sumando}")
suma()
