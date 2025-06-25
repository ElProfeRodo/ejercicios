numeros_pares=[]
N=int(input("ingrese una cifra"))
for i in range (0, N):
    c=i%2
    if c==0:
        numeros_pares.append(i)
print(numeros_pares)