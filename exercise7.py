class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("billai", 5)
cat2 = Cat("kaalaBillai", 3)
cat3 = Cat("gingercat", 2)


def get_oldest_cat(*args):
    return max(args)


print(
    f"The oldest cat is {get_oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")
