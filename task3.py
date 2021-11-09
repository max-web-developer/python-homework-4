# n=int(input('enter number: '))
# even=0
# odd=0
# while n>0:
#     n=n%10
#     if n%2==0:
#         even+1
#     else:
#         odd+1
#         n2=n%10
#         if n2%2==0:
#             even+1
#         else:
#             odd+1
#             n3=n2//10
#             if n3%2==0:
#                 even+1
#             else:
#                 odd+1
# print(even,odd)

n=int(input('enter number! '))
even=0
odd=0
while n>0:
    if n%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
print(even , odd )



