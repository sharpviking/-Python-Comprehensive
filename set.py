my_set = {1, 2, 3, 4, 5, 5}

my_set.add(2611)
my_set.add(5)

print(my_set)

# converting list into set

my_list = [1, 2, 3, 3, 4, 5, 7, 7]

print(set(my_list))


school = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}

# during class, the teachers take attendance and compile it into a list.
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

print(school.difference(attendance_list))
