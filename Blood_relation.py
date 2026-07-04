user_input = input("Enter the relation : ")
Gender = input(" Gender : ")
if user_input == ("Father" or "mother") and Gender == "M":
    print("son")
elif user_input == ("Mother"or "Father") and Gender == "F":
    print("daughter")
elif user_input == ("Brother" or "Sister") and Gender == "M":
    print("brother")
elif user_input == ("Brother" or "Sister") and Gender == "F":
    print("sister")