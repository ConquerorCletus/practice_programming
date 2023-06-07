from datetime import datetime

def calculate_date_difference(date1, date2):
    format = "%Y-%m-%d"
    date1_obj = datetime.strptime(date1, format)
    date2_obj = datetime.strptime(date2, format)
    difference = date2_obj - date1_obj
    years = difference.days // 365
    remaining_days = difference.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    return years, months, days

# Input two dates in "YYYY-MM-DD" format
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

# Calculate the difference between the dates
years, months, days = calculate_date_difference(date1, date2)

# Display the result
print(f"The difference between the dates is: {years} years, {months} months and {days} days")
