def decimalToBinary(num):
    if num == 0:
        return ""
    return decimalToBinary(num // 2) + str(num % 2)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(decimalToBinary(num))