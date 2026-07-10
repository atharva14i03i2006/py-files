arr = list(map(int, input().split()))
key = int(input("Enter element: "))

count = 0

for i in arr:
    if i == key:
        count += 1

print("Occurrences =", count)