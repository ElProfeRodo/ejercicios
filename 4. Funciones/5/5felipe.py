
def sumatoria(inicio,final):
    num=[]
    for i in range(inicio,final):
        if i%2!=0:
            num.append(i)
    suma=sum(num)
    print(suma)
sumatoria(0,15)