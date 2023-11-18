from functools import reduce

my_list = [26, 11, 35]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 3))
print(my_list)
