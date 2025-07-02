listado_av = {}

"""
listado_av = {
    'A001': {
        'nombre': 'Alejandro',
        'edad': 30,
        'puntajes': []
    },
    'A002': {
        'nombre': 'Alejandro',
        'edad': 30,
        'puntajes': []
    },
    'A003': {
        'nombre': 'Alejandro',
        'edad': 30,
        'puntajes': []
    }
}
"""

def registra_av(aventureros, codigo_av, datos_av):
    if codigo_av not in aventureros:
        aventureros[codigo_av] = {
            'nombre': datos_av[0],
            'edad': datos_av[1], 
            'puntajes': []
        }
        return True
    else:
        return False

def registra_puntaje(aventureros, codigo_av, puntaje):
    if codigo_av in aventureros:
        aventureros[codigo_av]['puntajes'].append(puntaje)
        return True
    else:
        return False

while True:
    print("1. Registrar aventureros con su código único, nombre y edad.")
    print("2. Registrar puntajes obtenidos por sesión para cada aventurero.")
    print("3. Modificar un puntaje específico de una sesión dada.")
    print("4. Visualizar el total acumulado y el promedio de puntajes por aventurero.")
    print("5. Mostrar los aventureros cuyo promedio de puntajes esté por debajo de un umbral dado.")
    print("6. Listar todos los aventureros con sus datos y puntajes.")
    print("7. Filtrar los aventureros por edad específica.")
    print("8. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        if registra_av(listado_av, codigo, [nombre, edad]):
            print("Registro exitoso")
        else:
            print("El código ya existe")
    elif opcion == 2:
        codigo = input("Código: ")
        puntaje = int(input("Puntaje: "))
        registra_puntaje(listado_av, codigo, puntaje)
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
