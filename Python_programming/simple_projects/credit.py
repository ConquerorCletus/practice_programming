print("If you want to buy this house. You must have good credit status")
credit_status = input("Enter your credit status (1 - 100): ")

credit_status = int(credit_status)
if credit_status > 50:
    print("You have good credit status.")
    print("You can put down 10% for the house")
elif credit_status < 50:
    print("You have a bad Credit status")
    print("Sorry you have to put down 20% for the house")
else:
    print("Input your credit status")
