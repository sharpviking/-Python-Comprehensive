#  continue keeps returning to the loop and prevents from printing

my_list = [1, 2, 3, 4, 5, 7]
for items in my_list:
    continue
    print(items)


i = 0
while i < len(my_list):
    continue
    print(my_list[i])
    i += 1
