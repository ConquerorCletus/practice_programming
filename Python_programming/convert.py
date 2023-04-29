weight = input("Input your weight (pounds):")
mass = float(weight) / 2.2046
print("Your weight is {}kg ".format(mass))
# This program collect user weight as string as store it as a float value.
print("____________END OF PROGRAM____________________")
print("_______________NEW PROGRAM_____________________")
new_weight = input("Input your weight: ")
new_weight = int(new_weight)
choice = input("is your weight in (L)bs or (K)g: ")

if choice.upper == "L":
    new_weight = new_weight * 2.2046
    print("Your weight is {} kg".format(new_weight))
    
else:
    new_weight = new_weight / 2.2046
    print("Your weight is {} pounds".format(new_weight))

