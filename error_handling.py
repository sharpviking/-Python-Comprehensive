while True:
    try:
        age = int(input('what is your is your age?'))
        10/age
        raise ValueError"'hey cut it out"

    except ZeroDivisionError:
        print('please enter a number higher than zero')
        break
    else:
        print('thank you!')

    finally:
        print('ok, i am finally done')

    print('can you hear me?')
