n = int(input("Enter a number: "))
print("hollow square pattern of ", n)
for i in range(1,n+1):
    if i == n or i == 1:
     print("*"*n,end="")
     print("\n", end ="")
    else:
       print("*",end="")
       print(" "*(n-2),end="")
       print("*",end="")
       print("\n",end="")