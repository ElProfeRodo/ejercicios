libros = {}
estado = {}

def registrar_libro(libros: dict, estado: dict, codigo: str, datos: list) -> bool:
    if codigo not in libros:
        libros[codigo] = [datos[0], datos[1], datos[2], datos[3]]
        estado[codigo] = ['disponible', None]
        return True
    return False

def prestar_libro(estado: dict, codigo: str, lector: str) -> bool:
    if codigo in estado and estado[codigo][0] == 'disponible':
        estado[codigo][0] = 'prestado'
        estado[codigo][1] = lector
        return True
    return False

def devolver_libro(estado: dict, codigo: str) -> bool:
    if codigo in estado and estado[codigo][0] == 'prestado':
        estado[codigo][0] = 'disponible'
        estado[codigo][1] = None
        return True
    return False

def listar_disponibles(libros: dict, estado: dict) -> None:
    for codigo, datos in libros.items():
        if estado[codigo][0] == 'disponible':
            print(f"Código: {codigo}, Título: {datos[0]}, Autor: {datos[1]}")
    else:
        print("\nNo hay libros para mostrar\n")

def listar_prestamos(libros: dict, estado: dict) -> None:
    for codigo, datos in libros.items():
        if estado[codigo][0] == 'prestado':
            print(f"Código: {codigo}, Título: {datos[0]}, Autor: {datos[1]}, Lector: {estado[codigo][1]}")
    else:
        print("\nNo hay libros para mostrar\n")

while True:
    print("1. Registrar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Listar disponibles")
    print("5. Listar prestados")
    print("6. Salir")

    try:
        opcion = int(input("Opción: "))
    except:
        print("Debe ser un valor numérico")
        continue

    if opcion == 1:
        codigo = input("Código: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        editorial = input("Editorial: ")
        anio = int(input("Año: "))
        if registrar_libro(libros, estado, codigo, [titulo, autor, editorial, anio]):
            print("\nLibro registrado\n")
        else:
            print(f"\nEl código {codigo} ya existe\n")

    elif opcion == 2:
        codigo = input("Código: ")
        lector = input("Lector: ")
        if prestar_libro(estado, codigo, lector):
            print("\nLibro prestado\n")
        else:
            print("\nEl libro no existe o no está disponible\n")

    elif opcion == 3:
        codigo = input("Código: ")
        if devolver_libro(estado, codigo):
            print("\nLibro devuelto\n")
        else:
            print("\nEl libro no se puede devolver\n")

    elif opcion == 4:
        listar_disponibles(libros, estado)

    elif opcion == 5:
        listar_prestamos(libros, estado)

    elif opcion == 6:
        break

    else:
        print("\nLa opción es incorrecta\n")
