n = int(input("Enter a Binary Number (0 and 1) : \n"))
decimal = 0
power = 0

while n > 0:
    digit = n % 10
    decimal += digit * (2 ** power)
    power += 1
    n //= 10
print(f"Decimal Number of {n} is : \n {decimal}")
