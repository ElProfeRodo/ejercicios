listado_estudiantes = {}

"""
listado_estudiantes = {
    "456-8": {
        "nombre": "Juan",
        "sesiones": [16, 25, 30, 45]
    }
}
"""

def registrar_estudiante(estudiantes, rut_est, nombre_est):
    if rut_est not in estudiantes:
        estudiantes[rut_est] = {'nombre': nombre_est, 'sesiones': []}
        return True
    else:
        return False

def registrar_participacion(estudiantes, rut_est, puntaje_est):
    if rut_est in estudiantes:
        estudiantes[rut_est]['sesiones'].append(puntaje_est)
        return True
    else:
        return False

def actualizar_participacion(estudiantes, rut_est, sesion, nuevo_puntaje):
    if rut_est in estudiantes:
        estudiantes[rut_est]['sesiones'][sesion] = nuevo_puntaje
        return True
    else:
        return False

def calcular_total_y_promedio(estudiantes, rut_est):
    if rut_est in estudiantes:
        for rut, datos in estudiantes.items():
            if rut == rut_est:
                #total = sum(datos['sesiones'])
                total = 0
                for puntaje in datos['sesiones']:
                    total += puntaje
                if len(datos['sesiones']) > 0:
                    promedio = total / len(datos['sesiones'])
                else:
                    promedio = 0
                print(f"{datos['nombre']} ({rut}) - Total: {total}, Promedio: {promedio}")
                break

def mostrar_estudiantes(estudiantes):
    for rut, datos in estudiantes.items():
        #total = sum(datos['sesiones'])
        total = 0
        for puntaje in datos['sesiones']:
            total += puntaje
        if len(datos['sesiones']) > 0:
            promedio = total / len(datos['sesiones'])
        else:
            promedio = 0
        print(f"{datos['nombre']} ({rut}) - Total: {total}, Promedio: {promedio}")

def participacion_baja(estudiantes, umbral):
    for rut, datos in estudiantes.items():
        #total = sum(datos['sesiones'])
        total = 0
        for puntaje in datos['sesiones']:
            total += puntaje
        if len(datos['sesiones']) > 0:
            promedio = total / len(datos['sesiones'])
        else:
            promedio = 0
        if promedio < umbral:
            print(f"{datos['nombre']} ({rut}) - Total: {total}, Promedio: {promedio}")

while True:
    print("1. Registrar un nuevo estudiante.")
    print("2. Registrar puntaje por sesión.")
    print("3. Modificar un puntaje anterior.")
    print("4. Ver todos los estudiantes con su total de puntajes y su promedio de puntajes.")
    print("5. Ver estudiantes con baja participación.")
    print("6. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        rut = input("RUT: ")
        nombre = input("Nombre: ")
        if registrar_estudiante(listado_estudiantes, rut, nombre):
            print("Registro realizado")
        else:
            print("El rut ya existe")

    elif opcion == 2:
        rut = input("RUT: ")
        puntaje = int(input("Puntaje: "))
        if registrar_participacion(listado_estudiantes, rut, puntaje):
            print("El puntaje fue agregado")
        else:
            print("El estudiante no existe")

    elif opcion == 3:
        rut = input("RUT: ")
        sesion = int(input("Sesión: "))
        nuevo_puntaje = int(input("Nuevo puntaje: "))
        if actualizar_participacion(listado_estudiantes, rut, sesion, nuevo_puntaje):
            print("El puntaje fue actualizado")
        else:
            print("El estudiante no existe")

    elif opcion == 4:
        rut = input("RUT: ")
        calcular_total_y_promedio(listado_estudiantes, rut)

    elif opcion == 5:
        umbral = float(input("Umbral: "))
        participacion_baja(listado_estudiantes, umbral)

    elif opcion == 6:
        break

    else:
        print("La opción ingresada es incorrecta")
