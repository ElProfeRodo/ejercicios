palabra = input('Ingrese un palindromo: ')
alreves = ''
for i in range(1, len(palabra)+1):
    alreves =  alreves + palabra[i*-1] 

if alreves == palabra:
    print('Su palabra es un palindromo :]')
else: 
    print('Su palabra no es un palindromo :[')