print('''

_________________________WELCOME TO LUCKY NUMBER______________________________________



        YOU ARE GOING TO GUESS A NUMBER BETWEEN 1 - 10
(1)IF YOUR NUMBER IS CORRECT THEN YOU WIN!!!
(2)YOU ARE GIVEN 3 TRIALS SO MAKE GOOD USE OF IT.
(3)THE PROGRAM TERMINATES WHEN YOU WIN


_____________________ARE YOU LUCKY? THE GAME STARTS NOW_______________________________''')
luckyNumber = 3
trial_count = 0
trial_limit = 3
while trial_count < trial_limit:
    number = int(input("Guess a number between 1 - 10: "))
    trial_count += 1

    if number == luckyNumber:
        print("YOU GUESSED THE LUCKY NUMBER!!! YOU ARE LUCKY INDEED.")
        break

    else:
        print("YOU ARE NOT LUCKY TODAY, TRY AGAIN!!!!")