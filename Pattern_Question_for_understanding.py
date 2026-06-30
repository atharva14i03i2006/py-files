'''
Right Triangle

'''
class Right_triangle():
    n = int(input("Enter a number : "))
    for i in range(1, n+1):
        print("*" * i, end ="\n")
        i += 1
Right_triangle()


'''
inverted triangle

'''

class Inverted_triangle():
    n = int(input("Enter a number : "))
    for i in range(n):
        print(" " * i + "*" *(2*(n-i)-1))
Inverted_triangle()

'''
Inverse Right triangle

'''

class Inverse_Right_triangle():
    n = int(input("Enter a number : "))
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * i)
Inverse_Right_triangle()

'''
Inverted Right Triangle

'''

class Inverted_Right_Triangle():
    n = int(input("Enter a number : "))
    for i in range(n):
        print("*"*(n-i)+" "*i)
Inverted_Right_Triangle()

'''
Inverse And Inverted Right Triangle

'''
class Inverse_Inverted_Right_Triangle():
    n = int(input("Enter a number : "))
    for i in range(n):
        print(" " * i + "*" * (n-i))
Inverse_Inverted_Right_Triangle()

'''
Triangle

'''
class Triangle():
    n = int(input("Enter a number : "))
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * (2*i-1))
Triangle()

'''
Diamond

'''
class Diamond():
    n = int(input("Enter a  number : "))
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (2*i-1))
    for j in range(1,n):
        print(" " * j + "*" * (2*(n-j)-1))