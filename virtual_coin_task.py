import random as rand
press = int(input('press 1 to toss the coin'))


if press:
    a = rand.randint(0,1)
    if a == 0:
        print('TAILS')
    else:
        print('HEADS')
else:
    print('Bye')