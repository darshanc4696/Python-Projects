print("----------PIZZA ORDER PROGRAM------------\n pizza and its cost\n 1.small pizza=100\n 2.medium pizza=200\n 3.large pizza=300")
n=int(input('enter your choice\n'))
if n==1:
    a=int(input('do you need pepperoni and extra cheese for this pizza:\nif only pepperoni then enter 1\nif ony extra cheese then enter 2\nif both then enter 3\nif you no need any of this then enter 0\n'))
    if a==0:
        print('your pizza cost is 100')
    elif a==1:
        print('your pizza cost is:130')
    elif a==2:
        print("your pizza cost is:120")
    elif a==3:
        print("your pizza cost is:150")
    else:
        print("number not valid once again order the pizza")
elif n==2:
    a=int(input('do you need pepperoni and extra cheese for this pizza:\nif only pepperoni then enter 1\nif ony extra cheese then enter 2\nif both then enter 3\nif you no need any of this then enter 0\n'))
    if a==0:
        print('your pizza cost is 200')
    elif a==1:
        print('your pizza cost is:250')
    elif a==2:
        print("your pizza cost is:220")
    elif a==3:
        print("your pizza cost is:270")
    else:
        print("number not valid once again order the pizza")
elif n==3:
    a=int(input('do you need pepperoni and extra cheese for this pizza:\nif only pepperoni then enter 1\nif ony extra cheese then enter 2\nif both then enter 3\nif you no need any of this then enter 0\n'))
    if a==0:
        print('your pizza cost is 300')
    elif a==1:
        print('your pizza cost is:350')
    elif a==2:
        print("your pizza cost is:320")
    elif a==3:
        print("your pizza cost is:370")
    else:
        print("number not valid once again order the pizza")
else:
    print("invalid number")










