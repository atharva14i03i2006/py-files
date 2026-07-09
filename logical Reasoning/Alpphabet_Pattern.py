class Alphabet_pattern:
    def __init__(self):
        self.rows = int(input("Enter the number of rows : "))
    def print_pattern(self):
        for i in range(1, self.rows + 1):
            print(chr(64 + i) * i)
        # different pattern 

        print(" diff pattern ")
        for i in range(1, self.rows + 1):
            for j in range(1 , i +1):
                print(chr(64 + j), end = "")
            print()

Alphabet_pattern().print_pattern()
    