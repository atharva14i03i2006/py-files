'''
Matrix Rotation Layer by Layer (Clockwise - 1 Step)
'''

print("\033[1mMatrix Rotation Layer By Layer\033[0m")

rows = int(input("Enter Number of Rows: "))
cols = int(input("Enter Number of Columns: "))

print("Enter Matrix:")
A = [list(map(int, input().split())) for _ in range(rows)]

top = 0
bottom = rows - 1
left = 0
right = cols - 1

while top < bottom and left < right:

    prev = A[top + 1][left]

    # Top Row
    for i in range(left, right + 1):
        A[top][i], prev = prev, A[top][i]

    top += 1

    # Right Column
    for i in range(top, bottom + 1):
        A[i][right], prev = prev, A[i][right]

    right -= 1

    # Bottom Row
    for i in range(right, left - 1, -1):
        A[bottom][i], prev = prev, A[bottom][i]

    bottom -= 1

    # Left Column
    for i in range(bottom, top - 1, -1):
        A[i][left], prev = prev, A[i][left]

    left += 1

print("\nRotated Matrix:")

for row in A:
    print(*row)
