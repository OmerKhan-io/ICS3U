import math as m
#Part 1 

print("Welcome to the even and odd detector!") # prints introductory statement
num1 = int(input("Enter your first number")) # asks the user to input his first number. 
#I used int to convert the input statement from a string to an integer.
num2 = int(input("Enter your second number")) #asks the user to input his second number. 
#I used int to convert the input statement from a string to an integer.

if (num1 % 2 == 0 and num2 % 2 == 0): #Checks if both number are even, by checking the remainder, This is because two goes into all even numbers, so no remainders 
  print("The product of both numbers are even")  #If both numbers are even, their product is even.
elif(num1 % 2 == 1 and num2 % 2 == 1): # Checks if both numbers are odd. This is because two does not go equally into odd numbers, so there will be a remainder of 1.
  print("The product of both numbers are odd")  #If both numbers are odd, their product is odd.
elif(num1 % 2 == 1 and num2 % 2 ==0): #Checks if num1 is odd and num2 is even. 
  print("The product of both numbers are even ") #If one is even and the other is odd, their product is even
else:
  print("The product of both numbers are even ") #There is only one possibility left, which is num1 is even and num2 is odd.In that case else statement is sufficient. 
  #If one is even and the other is odd, their product is even.

#Part 2
print("I will find the cube's inner diagonal for any edge length!") # Prints an introduction to the program.
iput = int(input("Please enter the edge length of your cube: ")) # Asks the user to input the edge length and converts it into an integer.

d = iput * m.sqrt(3) # Multiplies the user input value, which is stored in the variable 'iput', to the square root of 3. The result is stored in the variale 'd'
# Calculates the inner diagonal of the cube using the formula: diagonal = edge length * sqrt(3).
print("The length of the inner diagonal of a cube with the side length of  %.f is: %.2f" % (iput ,d))
# Prints the result using formatted string placeholders:
# %.f -> Represents the whole number value of `iput`
# %.2f -> Represents `d` rounded to 2 decimal places.

#Part 3
 
c = int(input("Please enter the amount of change in cents: ")) # Asks the user to input the amount of change in cents and converts it into an integer. 
# The user input will be stored in the variable 'c'

# Initializing variables for different coin denominations.
q = 0 #Number of quarters (25 cents)
d = 0 #Number of dimes (10 cents)
n = 0 #Number of nickels (5 cents)
p = 0 #Number of pennies (1 cent)
change = 0 # variable to track the remaining change.

if c >= 100:
   change = change % 100

if c >= 25:
   q = c // 25
   change = c % 25
   print("Number of quarters %d: " % q, end = "")

if c >= 10:
   d = c//10
   change = c % 10
   print("Number of dimes %d: " % d, end = "")
  
if c >= 5:
   n = c//5
   change = c%5
   print("Number of nickels %d: " % n, end = "")

if c >=1:
  print("Number of pennies %d: " % n, end = "")
   

   
