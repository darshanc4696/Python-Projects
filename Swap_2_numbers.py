def swap(a, b):
    temp = 0
    temp = a
    a = b
    b = temp
    return a, b


a = int(input('Enter value of a:'))
b = int(input('Enter value of b:'))
a, b = swap(a, b)
print(f"'a':{a} , 'b':{b}")
