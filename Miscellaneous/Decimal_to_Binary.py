import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Recursion.Decimal_to_Binary import decimalToBinary
num = int(input("Enter a number :"))

if num == 0:
    print(0)
else:
    print(decimalToBinary(num))