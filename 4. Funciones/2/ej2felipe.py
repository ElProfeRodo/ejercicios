def años():
    edad=int(input("ingrese su edad: "))
    while edad>=18:
        print("eres mayor de edad")
        break
    else:
        print("eres menor de edad")
        
años()