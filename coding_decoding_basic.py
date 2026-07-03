class CodingDecoding:
    def __init__(self):
        self.text = input("Enter a lowercase string: ")

    def encode(self):
        result = ""

        for i in range(len(self.text)):
            ch = self.text[i]

            # Shift according to position (1,2,3...)
            shift = i + 1

            # Convert to 0-25
            new_char = (ord(ch) - ord('a') + shift) % 26

            # Convert back to character
            result += chr(new_char + ord('a'))

        print("Encoded String:", result)


obj = CodingDecoding()
obj.encode()