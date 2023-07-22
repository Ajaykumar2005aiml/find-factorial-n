n=int(input("enter a value for factorial calculation: "))
ans=1
for i in range(1, n + 1):
    if n>0:
        ans=ans*i
    elif n==0:
        print("0 factorial is 1")
    else:
        print("factorial cant calculated for negative int ")
print(ans)

#(or)

import math
while True:
    n = int(input("enter a value for factorial calculation: "))
    a=math.factorial(n)
    print(a)
