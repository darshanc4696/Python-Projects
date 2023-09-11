import random

names = input('Enter the all your names separated by comma to decide who will pay for bill:')
names_split = names.split(',')
print(names_split)

rand = random.randint(0,len(names_split)-1)   # or we can use random.choice(names_split)
print(f'{names_split[rand]} is the bill payer')
