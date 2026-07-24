'''
caeasar_cipher
'''
s = input("Enter a string: ")
n = int(input("Enter the shift value: "))

result = ""
n = n % 26  

for ch in s:
    if ch.isupper():
        new_ch = chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        result += new_ch
    elif ch.islower():
        new_ch = chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        result += new_ch
    else:
        result += ch

print("Encrypted text:", result)
