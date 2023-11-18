my_list = [26, 11, 33]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))

print(my_list)
