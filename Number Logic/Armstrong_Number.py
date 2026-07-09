n = int(input("Enter a number: "))

temp = n
digits = len(str(n))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == n:
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")