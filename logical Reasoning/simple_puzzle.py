'''
Happy number 
Basically it is a number that is eventually becomes 1 when repeatedly
replaced by the sum of the square of its digits.
'''

n = int(input("Enter a number : "))
print("Checking whether the number is happy or not")
class Happy_number():
    def __init__(self, n):
        self.n = n
        
    def is_happy(self):
        hash_set = set()
        while self.n != 1 and self.n not in hash_set:
            hash_set.add(self.n)
            self.n = sum(int(i) ** 2 for i in str(self.n))
        print(f"The number is happy {n} ") if self.n == 1 else print(f"The number is not happy {n}")
        return self.n == 1
Happy_number(n).is_happy()