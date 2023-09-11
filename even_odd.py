def even_or_odd(n):
    if n % 2 == 0:
        print(f'{check_nu} is even.')
    else:
        print(f'{check_nu} is odd.')


check_nu = int(input('Enter the number to check whether it is even or odd:'))
even_or_odd(check_nu)