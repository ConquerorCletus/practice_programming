import random

def coin_toss():
    # Generate a random number (0 or 1)
    result = random.randint(0, 1)
    
    if result == 0:
        return "Heads"
    else:
        return "Tails"

num_tosses = int(input("Enter the number of coin tosses: "))

for _ in range(num_tosses):
    toss_result = coin_toss()
    print(toss_result)
