my_set = {1, 2, 3, 4, 4, 5}
your_set = {4, 5, 6, 8, 9, 11, 26}


print(my_set.difference(your_set))
my_set.discard(5)

print(my_set)

my_set.difference_update(your_set)


print(my_set)

print(my_set.intersection(your_set))

print(my_set.isdisjoint(your_set))

print(my_set.union(your_set))

print(my_set.issubset(your_set))

print(your_set.issuperset(my_set))
