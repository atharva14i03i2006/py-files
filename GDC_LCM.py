a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)

max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        print("LCM =", max_num)
        break
    max_num += 1