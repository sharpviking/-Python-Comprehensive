my_list = [1, 2, 3, 4, 5, 7]
for items in my_list:
    print(items)


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1


while True:
    response = input('say something:')
    if (response == 'bye'):
        break
