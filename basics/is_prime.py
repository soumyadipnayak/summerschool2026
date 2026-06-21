def is_prime(number: int) -> bool:
    if number <= 0:
        return False
    elif number == 1 or number == 2:
        return True
    else:
        for i in range(2, int(number**(1/2))+1):
            if number % i == 0:
                return False
        return True
    
number = int(input("Enter number=>"))
if is_prime(number):
    print("Number is prime")
else:
    print("Number is not prime")