"""
  Author : Omer Khan
  Student Number : 753619
  Revison date : 21 March 2025
  Program : A number guessing game 
  Description : guessing a number between 1 and 100
VARIABLE DICTIONARY
  tries = the number of tries for the user
  guess = the user input for the each guess
"""
import random # imports the random module to generate random numbers
#prints the welcome message for the game.
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
print("You have a maximum of six (6) tries.")
#Generates a random number between 1 and 100 for the user to guess
r = random.randint(1,100)
tries = 0 #initializing the number of tries to zero

# Start of the while loop, allowing the user a maximum of 6 tries
while tries < 6: #Stays in loop as long as tries is less than 6
  tries += 1 #adds 1 to tries each time
  # User input for the guess. prompts the user and converts it into an integer
  guess = int(input("Guess #%d: " % tries)) #using format
  if guess > r: # Check if the guess is higher than the random number
    print("Lower!") # If guess is higher it will tell the user to guess lower
  elif guess < r: # Check if the guess is lower than the random number
    print("Higher") # If guess is lower it will tell the user to guess higher
  else:
    print("Congragulations you got it") 
    
if guess != r: #Checks if the user input is not equal to r
  #if guess are incorrect after 6 tries, it will display the correct answer
  print("Sorry: No more guesses! The correct answer was %d. Good Luck next time" % r)
  
#The end of the program
