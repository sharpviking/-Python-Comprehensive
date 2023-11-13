# for items in (1, 2, 3, 4, 5):
#     for x in ["a", "b", "c"]:
#         print(items, x)

# dictoinary iterables

user = {
    "name": 'Frodo',
    'age': 29,
    "can_survive": True
}

for item in user.items():
    print(item)


for item in user.values():
    print(item)

for item in user.keys():
    print(item)


for key, value in user.items():
    print(key, value)
