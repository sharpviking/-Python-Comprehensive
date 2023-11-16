class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def run(self):
        print('run')
        return ('done')


player1 = PlayerCharacter("Adithi", 44)
player2 = PlayerCharacter("Anand", 45)

print(player1.name)
print(player2.age)
