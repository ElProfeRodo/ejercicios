def can_nombre(nombre):
    if len(nombre) >= 6:
        return True
    return False

def mascota_nombre():
    nombre = input("Ingrese el nombre de su mascota: ")
    return can_nombre(nombre)

print(mascota_nombre())
