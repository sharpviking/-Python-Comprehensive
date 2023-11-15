def super_func(*args, **kwargs):

    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(2, 3, 5, 8, 9, 7, num1=11, num2=26))
