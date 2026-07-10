n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input()))

result = []

for i in lst:
    if i not in result:
        result.append(i)

print(result)