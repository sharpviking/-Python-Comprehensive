from random import randint


# generate a number
answer = input('input a number 1~10')

# input from user?


# check that input is a number
while True:
    try:
        guess = int(input("guess a number 1~10:  "))
        if int(guess) > 0 and int(guess) < 11:
            if guess == answer:

                print("you are a genious")
                break

    except ValueError:
        print('please enter a number')
        continue
