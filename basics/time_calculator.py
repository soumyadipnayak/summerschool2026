total_seconds = int(input("Enter total seconds: "))
hours = total_seconds // 3600
partial_hours = total_seconds % 3600
minutes = partial_hours // 60
seconds = partial_hours % 60
print(f"Time: {hours} hours, {minutes} minutes, {seconds} seconds")
