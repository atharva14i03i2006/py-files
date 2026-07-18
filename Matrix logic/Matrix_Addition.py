r = int(input("Rows: "))
c = int(input("Columns: "))

print("Enter Matrix A")
A = [list(map(int, input().split())) for _ in range(r)]

print("Enter Matrix B")
B = [list(map(int, input().split())) for _ in range(r)]

result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Result:")
for row in result:
    print(*row)