'''
On Going ..
'''

print("\033[1m* Matrix Spiral Traversal *\033[0m")

rows = int(input("Enter Rows: "))
cols = int(input("Enter Columns: "))

matrix = []

print("\nEnter Matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

top = 0
bottom = rows - 1
left = 0
right = cols - 1

spiral = []

while top <= bottom and left <= right:

    # Left to Right
    for j in range(left, right + 1):
        spiral.append(matrix[top][j])
    top += 1

    # Top to Bottom
    for i in range(top, bottom + 1):
        spiral.append(matrix[i][right])
    right -= 1

    # Right to Left
    if top <= bottom:
        for j in range(right, left - 1, -1):
            spiral.append(matrix[bottom][j])
        bottom -= 1

    # Bottom to Top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            spiral.append(matrix[i][left])
        left += 1

print("\nSpiral Traversal:")
print(*spiral)