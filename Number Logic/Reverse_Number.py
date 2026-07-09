n = int(input("Enter a number : "))
Reverse_num = 0
while n > 0:
    digit = n % 10
    Reverse_num = Reverse_num * 10 + digit
    n = n // 10
print("Reversed number :", Reverse_num)