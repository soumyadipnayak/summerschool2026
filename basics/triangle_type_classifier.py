side1 = float(input("Enter side1 length: "))
side2 = float(input("Enter side2 length: "))
side3 = float(input("Enter side3 length: "))

if (side1 <= 0 or side2 <= 0 or side3 <= 0) or (side1+side2 <= side3) or (side1+side3 <= side2) or (side2+side3 <= side1):
    print("Invalid triangle")
else:
    if (side1==side2) and (side2==side3):
        print("Equilateral")
    elif (side1==side2) or (side2==side3) or (side3==side1):
        print("Isosceles")
    else:
        print("Scalene")
