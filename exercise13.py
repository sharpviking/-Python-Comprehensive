# Naive way
some_list = ['a', 'b', 'c', 'b', 'a', 'd', 'd', 't', 'h', 'i', 'n', 'd']


duplicates = []
for values in some_list:
    if some_list.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)

print(duplicates)

# List comprehensiuon way
some_list1 = ['a', 'b', 'c', 'b', 'a', 'd', 'd', 't', 'h', 'i', 'n', 'd']

duplicates1 = list(set([x for x in some_list1 if some_list1.count(x) > 1]))

print(duplicates1)
