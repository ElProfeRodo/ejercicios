'''
Crear una función que reciba como parámetro un nombre y un apellido, genere la
dirección de correo electrónico Gmail con esos datos y muestre por pantalla el
resultado.
'''
def correo_elec(nom, apell):
    correo = nom+'.'+apell+"@gmail.com"
    return correo 

nom = input("ingrese su nombre: ")
apell = input("ingrese su apellido: ")
print (correo_elec(nom,apell))
