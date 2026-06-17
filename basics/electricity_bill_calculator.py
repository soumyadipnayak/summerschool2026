total_units = int(input("Enter total units consumed=>"))

# Ignoring handling negative unit consumption e.g. on-grid renewable energy solutions
# if total_units < 0:
#     print("Please double check the total consumption!")

if total_units <= 100:
    total_bill = total_units * 5

elif total_units <= 200:
    total_bill = (100 * 5) + ((total_units - 100) * 7)

else:
    total_bill = ((100 * 5) + (100 * 7) + ((total_units - 200) * 10))

print(f"Total bill: ₹{total_bill}")
