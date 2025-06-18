def mini_calculadora(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    try:
        division = num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        division = 0
    print(f"La suma de los numeros es {suma}")
    print(f"La resta de los numeros es {resta}")
    print(f"La multiplicacion de los numeros es {multiplicacion}")
    print(f"La division de los numeros es {division}")
mini_calculadora(5, 2)