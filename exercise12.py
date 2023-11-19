
# Square
my_list = [26, 11, 92]


print(list(map(lambda item: item**2, my_list)))

# List shorting

a = [(0, 2), (4, 3), (9, 9), (10-1)]
a.sort(key=lambda x: x[1])
print(a)
