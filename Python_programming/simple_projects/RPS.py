import random
print('''
________________WELCOME TO ROCK, PAPER, SCISSORS GAME!!__________________


THE GAME BEGINS NOW:
ROCK, PAPER, SCISSORS!!!
ROCK, PAPER, SCISSORS!!!
ROCK(1), PAPER(2), SCISSORS(3)!!!


\t MAKE YOUR CHOICE BETWEEN BASED ON INDEX(1 - 3) 

''')
choices = ["ROCK", "PAPER", "SCISSORS"]
computer_choice = random.choice(choices)
player_choice = int(input("\nEnter your choice (1-3): "))
player_choice = choices[player_choice - 1]

print("\nYOU CHOSE", player_choice)
print("COMPUTER CHOSE", computer_choice)

if player_choice == computer_choice:
    print("\nIt's a tie!")
elif player_choice == "Rock":
    if computer_choice == "Paper":
        print("\nYou lose!")
    else:
        print("\nYou win!")
elif player_choice == "Paper":
    if computer_choice == "Scissors":
        print("\nYou lose!")
    else:
        print("\nYou win!")
else:
    if computer_choice == "Rock":
        print("\nYou lose!")
    else:
        print("\nYou win!")