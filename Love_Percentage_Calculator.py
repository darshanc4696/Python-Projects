print("------------------------LOVE PERCENTAGE CALCULATOR------------------------------------")
while True:
    nam1,nam2=input('Enter two names to calculate love % : \n').split()
    nam=nam1+nam2
    a=nam.lower()


    T=a.count('t')
    R=a.count('r')
    U=a.count('u')
    E=a.count('e')

    L=a.count('l')
    O=a.count('o')
    V=a.count('v')
    E=a.count('e')


    one=T+R+U+E
    two=L+O+V+E
    if str(one)+str(two)=='1010':
        print("your love percentage is 100%")
    else:
        print(f"your love percentage is {one}{two}%")
        i=int(str(one)+str(two))
        if i>90:
            print("you go together like a blast")
        elif 40<i<90:
            print('best ever')
        else:
            print('a good relationship')

    y = input('Press "y" to continue or "n" to exit : ')

    if y == "n":
        break

