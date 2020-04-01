# Create a simple number guessing game that gives the user 5 chances.
# Read the python 3 documentation for the "random.randint()" function.
# Use that function to generate a random integer between 0 and 10.
#
# Then, prompt them 5 times (at most) to guess the number.
#
# If they guess correctly, congratulate them, and do not prompt them any more.
# If they guess incorrectly, let them know they didn't guess correctly.
# If they run out of guesses, tell them they need to run the program again.

import random

r = random.randint(1, 10)


i = 0
c = True

while i < 5 and c == True:
    g = int(input("Guess an integer between 1 and 10: "))
    if g == r:
        print("You guessed {}, you're right! Congrats!".format(g))
        c = False
    else:
        i += 1
        print(
            "You guessed {}, that's incorrect. You have {} chances to guess correctly.".format(
                g, (5 - i)
            )
        )
        if i == 5:
            print(
                "\nThe correct answer was {}. Play again by running the script again.".format(
                    r
                )
            )
