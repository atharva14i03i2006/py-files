start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

print("Number of prime numbers =", count)