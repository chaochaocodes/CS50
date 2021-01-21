"""
Guessing Game
Write a program that picks a pseudorandom number between 1 and 10, 
inclusive, and gives the user up to 3 chances to guess that number. 
Each time printing some message informing the uesr whether or not their guess was correct.
"""

import random

number = random.randint(1,10)
for i in range(3):
  guess = int(input("Please enter your guess: "))
  if guess > number:
    print("Guess is too large")
  elif guess < number:
    print("guess is too small")
  else:
    print("Correct!")
    break
# while True:
#   try: 
#     guess = int(input("Please enter your guess: "))
#   except ValueError:
#     print("Sorry, please enter a number.")
#     # try again, return to start of loop
#     continue 
#   else:
#     break

# if num == number:
#   print('You guessed correctly!')
# elif num != number:
#   print('You have 2 more tries. Guess again')
# else:
#   print('Last chance! What is your final guess')
