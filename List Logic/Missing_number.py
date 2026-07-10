n = int(input("Enter value of n: "))

lst = []

print("Enter", n-1, "numbers")

for i in range(n-1):
    lst.append(int(input()))

total = n * (n + 1) // 2

print("Missing Number =", total - sum(lst))