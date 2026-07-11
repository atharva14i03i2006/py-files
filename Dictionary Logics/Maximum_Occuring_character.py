text = input("Enter a string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

max_char = max(freq, key=freq.get)

print("Maximum occurring character:", max_char)