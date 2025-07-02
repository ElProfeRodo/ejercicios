listado_av = {}

def registrar_aventurero(aventureros, codigo_av, datos_av):
    if codigo_av not in aventureros:
        aventureros[codigo_av] = {'nombre': datos_av[0], 'edad': datos_av[1], 'puntajes': []}
        return True
    return False

def registrar_puntaje(aventureros, codigo_av, puntaje):
    if codigo_av in aventureros:
        aventureros[codigo_av]['puntajes'].append(puntaje)
        return True
    return False

def modificar_puntaje(aventureros, codigo_av, sesion, nuevo_puntaje):
    if codigo_av in aventureros and nuevo_puntaje >= 0:
        try:
            aventureros[codigo_av]['puntajes'][sesion] = nuevo_puntaje
            return True
        except:
            return False
    return False

def mostrar_participacion(aventureros):
    for codigo, datos in aventureros.items():
        total = 0
        for puntaje in datos['puntajes']:
            total += puntaje
        if len(datos['puntajes']) > 0:
            promedio = total / len(datos['puntajes'])
        else:
            promedio = 0
        print(f"{datos['nombre']} ({codigo}) - Total: {total}, Promedio: {promedio}")

def participantes_con_bajo_promedio(aventureros, umbral):
    for codigo, datos in aventureros.items():
        total = 0
        for puntaje in datos['puntajes']:
            total += puntaje
        if len(datos['puntajes']) > 0:
            promedio = total / len(datos['puntajes'])
        else:
            promedio = 0
        if promedio < umbral:
            print(f"{datos['nombre']} ({codigo}), Edad {datos['edad']} y Puntaje {datos['puntajes']}")

while True:
    print("1. Registrar aventureros")
    print("2. Registrar puntajes")
    print("3. Modificar un puntaje específico")
    print("4. Visualizar el total acumulado y el promedio")
    print("5. Mostrar los aventureros por debajo de un umbral")
    print("6. Listar todos los aventureros")
    print("7. Filtrar los aventureros por edad")
    print("8. SALIR")
    
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        if registrar_aventurero(listado_av, codigo, [nombre, edad]):
            print("Registro realizado")
        else:
            print("El código ya existe")

    elif opcion == 2:
        codigo = input("Código: ")
        while True:
            try:
                puntaje = int(input("Puntaje: "))
                break
            except:
                print("Debe ser un número")
        if registrar_puntaje(listado_av, codigo, puntaje):
            print("El puntaje fue agregado")
        else:
            print("El código no existe")

    elif opcion == 3:
        codigo = input("Código: ")

        while True:
            try:
                sesion = int(input("Sesión: "))
                break
            except:
                print("Sesión debe ser un número")

        while True:
            try:
                nuevo_puntaje = int(input("Nuevo puntaje: "))
                break
            except:
                print("Nuevo puntaje debe ser un número")

        if modificar_puntaje(listado_av, codigo, sesion, nuevo_puntaje):
            print("El puntaje fue actualizado")
        else:
            print("El puntaje no fue actualizado")

    elif opcion == 4:
        mostrar_participacion(listado_av)

    elif opcion == 5:
        participantes_con_bajo_promedio(listado_av, 400)

    elif opcion == 6:
        pass
    elif opcion == 7:
        pass
    elif opcion == 8:
        break
    else:
        print("La opción es incorrecta\n")
