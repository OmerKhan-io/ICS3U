
import random
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
print("You have a maximum of six (6) tries.")
r = random.randint(1,100)
tries = 0 

while tries < 6:
  tries += 1
  guess = int(input("Guess #%d: " % tries))
  if guess > r:
    print("Lower!")
  elif guess < r:
    print("Higher")
  elif guess == r:
    print("You got it") 
    
if guess != r: #Checks if the user input is not equal to r
  print("Sorry: No more guesses! The correct answer was %d. Good Luck next time" % r)
