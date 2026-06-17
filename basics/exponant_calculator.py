base = int(input("Enter base=>"))
exponent = int(input("Enter exponent=>"))
result = 1
if exponent < 0:
    print("Only non-negative exponents are accepted for now!")
elif exponent == 0:
    print(f"Result = {result}")
else:
    while exponent >= 1:
        result *= base
        exponent -= 1
    print(f"Result = {result}")
