a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

if is_prime(a) and is_prime(b) and abs(a - b) == 2:
    print("Twin Prime Numbers")
else:
    print("Not Twin Prime Numbers")