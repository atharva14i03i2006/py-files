arr = list(map(int, input().split()))
key = int(input("Enter element: "))

for i in range(len(arr)-1, -1, -1):
    if arr[i] == key:
        print("Last occurrence at index", i)
        break
else:
    print("Element not found")