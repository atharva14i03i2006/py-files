n = int(input("Enter number of sides : "))
sides = list(map(int, input("Enter the sides of triangle : ").split()))
if len(sides) != n:
        print(f"Please enter exactly {n} sides. ")
else:

# check the number of triangles

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if sides[i] + sides[j] > sides[k] and sides[i] + sides[k] > sides[j] and sides[j] + sides[k] > sides[i]:
                    count += 1
    print("Number of triangles : ", count)