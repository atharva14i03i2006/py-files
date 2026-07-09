class Mirror_pattern():
    n = int(input("Enter the number of rows : "))
    def user_pattern(n):
        print("The user pattern is : ")
        for i in range(1, n + 1):
            print("*" * i)


    def mirror_pattern(n):
        print("The mirror pattern is : ")
        for i in range(n):
            print("*" * (n - i))
    user_pattern(n)
    mirror_pattern(n)
    