class Diamond_star_pattern():
    n = int(input("Enter the number of rows: "))

    # Upper Half
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))

    # Lower Half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))
Diamond_star_pattern()