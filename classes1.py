class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")


player1 = PlayerCharacter("Adithi", 44)
player2 = PlayerCharacter("Anand", 45)

print(player1.name)
print(player2.age)
