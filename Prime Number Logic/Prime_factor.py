n = int(input("Enter a number: "))

i = 2

print("Prime Factors are:")

while i <= n:
    while n % i == 0:
        print(i, end=" ")
        n = n // i
    i += 1