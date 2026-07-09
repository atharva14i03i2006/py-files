n = int(input("Enter Matrix Number : "))
for i in range(1, n+1):
    for j in range(1,n+1):
        print(i * j, end = "\t")
    print()