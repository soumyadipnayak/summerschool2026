limit = int(input("Enter upper limit=>"))
odd_sum = 0
if limit < 0:
    print("Only non-negative limits are accepted for now!")
else:
    while limit >= 0:
        if limit % 2 != 0:
            odd_sum += limit
        limit -= 1
    print(f"Sum of odd numbers in given limit = {odd_sum}")