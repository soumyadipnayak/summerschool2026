age = int(input("Enter age: "))
day = input("Enter day (weekday/weekend): ").lower()

if age < 5:
    price = 0
elif age <= 12:
    if 'weekday' in day:
        price = 100
    else:
        price = 150
elif age <= 60:
    if 'weekday' in day:
        price = 200
    else:
        price = 250
else:
    price = 100

print(f"Ticket price => {price}")