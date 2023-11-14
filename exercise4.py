my_list = ["a", "a", "i", "d", "c", "n", "b", "a", "n", "b"]


duplicates = []

for values in my_list:
    if my_list.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)

print(duplicates)
