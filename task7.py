# homewok by maks_kavlanov
n=int(input('eneter number: '))
n1=0
k=0
while n > 0:
    dijit=n % 10
    k+=1
    n1 = n+dijit/k
    n=n//10
    k+=1
print(n1)


