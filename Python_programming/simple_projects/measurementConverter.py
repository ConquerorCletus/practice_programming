# Input the length in centimeters
cm = float(input("Enter length in centimeters: "))

# Define conversion factors per cm
meters_per_cm = 0.01
kilometers_per_cm = 0.00001
inches_per_cm = 0.393701
feet_per_cm = 0.0328084

# Prompt the user to select a unit with the following character initials to convert to
unit = input("Convert to (m)eters, (k)ilometers, (i)nches, or (f)eet? ")

# Convert the length to the selected unit with conditional statements.
if unit == 'm':
    length = cm * meters_per_cm
    unit_name = 'meters'
elif unit == 'k':
    length = cm * kilometers_per_cm
    unit_name = 'kilometers'
elif unit == 'i':   
    length = cm * inches_per_cm
    unit_name = 'inches'
elif unit == 'f':
    length = cm * feet_per_cm
    unit_name = 'feet'
else:
    print("Invalid unit. Please select (m)eters, (k)ilometers, (i)nches, or (f)eet.")
    exit()

# Output the results
print("Length in {}: {:.2f}".format(unit_name, length))