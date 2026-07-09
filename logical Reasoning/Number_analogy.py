class Number_analogy:
    def __init__(self, num1 , num2 , num3):
        self.num1 = int(input("Enter the number: "))
        self.num2 = int(input("Enter the number: "))
        self.num3 = int(input("Enter the number: "))

    def Number_analogy(self):
        diff = self.num2 - self.num1
        self.num4 = self.num3 + diff
        print(f"{self.num1} : {self.num2} :: {self.num3} : {self.num4} the number analogy ")
Number_analogy(0, 0, 0).Number_analogy()