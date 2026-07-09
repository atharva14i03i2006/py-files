n = int(input("Enter number of columns: "))

for i in range(3):
    row = ""
    for j in range(n):
        if (i + j) % 4 == 0 or (i == 1 and j % 4 == 2):
            row += "* "
        else:
            row += "  "
    print(row)