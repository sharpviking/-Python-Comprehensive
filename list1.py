basket = [1, 2, 3, 4]

basket.extend([3, 101])
new_list = basket
print(basket)
print(new_list)


# Question

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")

basket.pop()

basket.append('kiwi')

basket.insert(0, "Apples")

basket.count("Apples")

basket.clear()

print(basket)


basket2 = ["a", "b", "c", "d", "e", "3", "7"]

# basket2.sort()
print(sorted(basket2))
print(basket2)

basket2.sort()
basket2.reverse()
print(basket2)
