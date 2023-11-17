class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")

    @classmethod
    def add_things(cls, num1, num2):
        return num1+num2


player1 = PlayerCharacter("Abhishek", 44)
player2 = PlayerCharacter("Anand", 45)

print(player1.name)
print(player2.age)

print(PlayerCharacter.add_things(26, 11))
