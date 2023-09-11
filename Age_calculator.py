maximum_age = int(input('Enter the max. age a human can live in this world:'))
current_age = int(input('Enter your current age:'))

years_left = maximum_age - current_age
days_left = years_left * 365
months_left = years_left * 12
week_left = years_left * 52

print(f"You have {days_left} days, {months_left} months, {week_left} week left to live on this world ")