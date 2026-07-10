arr = list(map(int, input().split()))
key = int(input("Enter element: "))

for i in range(len(arr)):
    if arr[i] == key:
        print("First occurrence at index", i)
        break
else:
    print("Element not found")