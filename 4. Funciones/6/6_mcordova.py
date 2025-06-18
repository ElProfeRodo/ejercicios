#6

def calculos(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    print(f'la suma es {suma} \nla resta es {resta} \nla multiplicacion es {multi}')
    try:
        division = num1 / num2
        print(division)
    except:
        print('no se puede realizar este calculo')
    
n1m = int(input('Ingrese el primer número: '))
n2m = int(input('Ingrese el segundo numero: '))

(calculos(n1m, n2m))
