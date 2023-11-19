sample_dict = {
    'a': 26,
    'b': 11
}

my_dict = {k: v**2 for k, v in sample_dict.items() if v % 2 == 0}

my_dict1 = {num: num**2 for num in [1, 2, 3]}
print(my_dict1)
