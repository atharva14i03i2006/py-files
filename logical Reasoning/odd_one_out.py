list = []
list.append(int(input("Enter a number : ")))
list.append(int(input("Enter a number : ")))
list.append(int(input("Enter a number : ")))
list.append(int(input("Enter a number : ")))
list.append(int(input("Enter a number : ")))
list.sort()
def Odd_one_out():
    if list[0] % 2 == 0 :
        print("The list is even")
        for i in range(len(list)):
            if list[i] % 2 != 0:
                print("The odd one out is : ", list[i])
    else:
        print("The list is odd")
        for i in range(len(list)):
            if list[i] %2 == 0:
                print("The odd one out is : ", list[i])
Odd_one_out()