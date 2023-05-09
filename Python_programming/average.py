def _average(numbers):
    total_of_numbers = sum(numbers)
    length = len(numbers)
    average = total_of_numbers / length
    return average

# Assuming this list of numbers is given before compile time
numbers = [4, 7, 15, 18, 20, 15]
avg = _average(numbers)
print(f"The average is {avg}")
