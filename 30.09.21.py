# задание 1
n1=int(input('enter number: '))
n2=0
while n1>0:
    dijit=n1%10
    n1=n1//10
    n2=n2*10
    n2=n2+dijit
print(n2)

