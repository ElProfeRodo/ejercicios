def pedir_edad():
    while True:
        try:
            edad = int (input("Ingrese Su Edad: "))
            return edad
        except:
            print ("ERROR, Introduce un numero valido")

def verif_mayoria_edad(edad):
    if edad >= 18:
        print ("eres mayor de edad")
    else:
        print ("eres menor de edad")

def main():
    edad = pedir_edad()
    verif_mayoria_edad(edad)

main()