n = int(input("Enter a number: "))

freq = [0] * 10

while n > 0:
    digit = n % 10
    freq[digit] += 1
    n //= 10

for i in range(10):
    if freq[i] != 0:
        print(i, "occurs", freq[i], "times")