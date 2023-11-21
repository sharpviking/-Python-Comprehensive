def generator_func(num):
    for i in range(num):
        yield i


for item in generator_func(2611):
    print(item)


# basic creation generator function
def gen_fun(num):
    for i in range(num):
        yield i


for item in gen_fun(100)