username = input("what is username?")

password = input("passwords please")

password_length = len(password)

hidden_password = '*' * password_length

print(f"{username}, your password is {hidden_password}, and it is {password_length} letters long.")
