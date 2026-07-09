class Floyd_Triangle():
    def triangle():
        n = int(input("Enter a number of rows: "))
        num = 1
        print("Floyd's Triangle : \n")

        for i in range(1, n+1):
            for j in range(1,i+1):
                print(num, end=" ")
                num +=1
            print()
Floyd_Triangle.triangle()