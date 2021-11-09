n=int(input('eneter number: '))
n1=0
n2=0
while n>0:
    dijit=n%10
    n1=n1+dijit
    n2=n2*dijit
    n=n//10
print(n1)
print(n2)