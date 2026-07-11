d = {"a": 1, "b": 2, "c": 3}

inv = {}

for key, value in d.items():
    inv[value] = key

print(inv)