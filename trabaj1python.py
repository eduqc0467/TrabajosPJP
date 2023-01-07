#PRograma para mostrar si el numero es divisible por 3 y 5
num=input("ingrese el numero")
sum=0
tam=len(num)
ult=int(num)%10
for i in range (tam):
    sum=sum + int(num[i])
div3=sum%3
if div3==0:
    print("El numero es divisible por 3")
div5=ult%5
if ult==5 or ult==0:
    print("El numero es divisible por 5")
