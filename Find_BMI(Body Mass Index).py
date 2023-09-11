print("--------------FINDING OUT THE BMI--------------")
weight = int(input('enter your weight in kg '))
height = float(input('enter your height in meter '))

BMI = weight / (height ** 2)

print(round(BMI))  # round(number,round of for no of digits)
