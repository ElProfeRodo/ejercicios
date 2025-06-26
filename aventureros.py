aventureros = {}

"""
aventureros = {
    'AV123': {
        'nombre': 'Kevin',
        'edad': 20,
        'puntaje': [100, 512]
    },

    'AV456': {
        'nombre': 'Marcela',
        'edad': 33,
        'puntaje': []
    }
}
"""

def registrar_aventurero(listado_av, codigo_av, nombre_av, edad_av):
    if codigo_av not in listado_av:
        listado_av[codigo_av] = {'nombre': nombre_av, 'edad': edad_av, 'puntaje': []}
        print("Aventurero registrado!")
    else:
        print("El código ya existe")

def agregar_puntaje(listado_av, codigo_av, puntaje):
    if codigo_av in listado_av:
        listado_av[codigo_av]['puntaje'].append(puntaje)
        print("Puntaje agregado")
    else:
        print("El código no existe")

while True:
    print("1. Registrar aventurero")
    print("2. Agregar puntaje de sesión")
    print("3. Modificar puntaje")
    print("4. Ver participación total y promedio")
    print("5. Ver aventureros con bajo promedio")
    print("6. Listar aventureros y puntajes")
    print("7. Listar aventureros por edad")
    print("8. SALIR")

    opcion = int(input("Opción: "))

    if opcion == 1:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        registrar_aventurero(aventureros, codigo, nombre, edad)
        print(aventureros)

    elif opcion == 2:
        codigo = input("Código: ")
        puntaje = int(input("Puntaje: "))
        agregar_puntaje(aventureros, codigo, puntaje)
        print(aventureros)

    elif opcion == 3:
        pass

    elif opcion == 4:
        pass

    elif opcion == 5:
        pass

    elif opcion == 6:
        pass

    elif opcion == 7:
        pass

    elif opcion == 8:
        break

    else:
        print("La opción es incorrecta")