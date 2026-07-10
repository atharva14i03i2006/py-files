n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input()))

k = int(input("Enter K: "))

k = k % n

result = lst[-k:] + lst[:-k]

print(result)