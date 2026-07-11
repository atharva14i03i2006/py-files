def perfect(n):
    s = 0

    for i in range(1, n):
        if n % i == 0:
            s += i

    return s == n

num = int(input("Enter number: "))

if perfect(num):
    print("Perfect Number")
else:
    print("Not Perfect")