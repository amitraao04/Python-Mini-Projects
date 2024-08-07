# Algorithm: Below are the Steps:
# 1) User inputs the lower bound and upper bound of the range.
# 2) The compiler generates a random integer between the range and stores it in a variable for future references.
# 3) For repetitive guessing, a while loop will be initialized.
# 4) If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
# 5) Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
# 6) And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
# 7) Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.

import random
import math

lower = int(input("Enter the lower bound : "))
upper = int(input("Enter the upper bound : "))

x = random.randint(lower,upper)
print("You have got",round(math.log(upper-lower+1,2)), "chances to guess.")

count = 0

while count < math.log(upper-lower+1,2):
    count+=1

    guess = int(input("Guess the number : "))

    if guess==x:
        print("Congratulations!!! You won the game!! The number was",x)
        break

    elif guess>x:
        print("Try again! You guessed too high.")

    elif guess<x:
        print("Try again! You guessed too low.")

if count > math.log(upper-lower+1,2):
    print("YOU LOSE!")
    print("The number was",x,"\n Better luck next time")
    