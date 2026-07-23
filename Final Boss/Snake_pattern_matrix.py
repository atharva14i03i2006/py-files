'''
Snake Pattern Matrix 
'''
print("/033[1m"Snake Pattern Matrix"[0m")
n = int(input("Enter a number of rows : /n")
A = [list(map(int , input("Enter a matrix :").split())) for _ in range(n)]
for i in range(1,n+1):
    if i % 2 == 0:
       for j in range(n):
         print(A[i][j], end=" ")
    else:
       for j in range(n - 1, -1 , -1):
         print(A[i][j], end=" ")
