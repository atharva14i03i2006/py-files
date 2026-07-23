'''
Snake Pattern Matrix 
'''
print("/033[1m"Snake Pattern Matrix"[0m")
n = int(input("Enter a number of rows : /n")
A = [list(map(int , input("Enter a matrix :").split())) for _ in range(n)]
for i in range(1,n+1):
    if i % 2 == 0:
       print("Left to right")
    else:
       print("Right to left")
