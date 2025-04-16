#### PART 1: EVEN OR ODD ####

"""
  Author : Omer Khan
  Student Number : 753619
  Revison date : 1 March 2025
  Program : Even or Odd
  Description : A program that determines whether the product of number is even or odd
VARIABLE DICTIONARY
  num1(int) = the first number inputted by the user
  num2(int) = the second number inputted by the user
  product(int) = The product (multiplication) of the first number and the second number.
"""

print("Welcome to the even and odd detector!") # prints introductory statement
num1 = int(input("Enter your first number: ")) # asks the user to input his first number. 
#I used int to convert the input statement from a string to an integer.
num2 = int(input("Enter your second number: ")) #asks the user to input his second number. 
#I used int to convert the input statement from a string to an integer.
product = num1*num2

if (num1 % 2 == 0 and num2 % 2 == 0): #Checks if both number are even, by checking the remainder, This is because two goes into all even numbers, so no remainders 
  print("The product of %d x %d (which is %d) will be even" % (num1, num2, product))  #If both numbers are even, their product is even.
elif(num1 % 2 == 1 and num2 % 2 == 1): # Checks if both numbers are odd. This is because two does not go equally into odd numbers, so there will be a remainder of 1.
  print("The product of %d x %d (which is %d) will be odd" % (num1, num2, product))  #If both numbers are odd, their product is odd.
elif(num1 % 2 == 1 and num2 % 2 ==0): #Checks if num1 is odd and num2 is even. 
 print("The product of %d x %d (which is %d) will be even" % (num1, num2, product)) #If one is even and the other is odd, their product is even
else: ##There is only one possibility left, which is num1 is even and num2 is odd.In that case else statement is sufficient. 
  print("The product of %d x %d (which is %d) will be even" % (num1, num2, product)) #If one is even and the other is odd, their product is even.

##### Part 2:  #####
"""
  Author : Omer Khan
  Student Number : 753619
  Revison date : 1 March 2025
  Program : Even or Odd
  Description : A program that determines the cube's inner diagonal for any edge length 
VARIABLE DICTIONARY
  iput(int) = the edge length inputted by the user
  d(float) = Stores the calculated inner diagonal of the cube using the formula:edge length multiplies by the square root of three
"""

import math as m #This imports the math module and gives it an alias 'm'
print("I will find the cube's inner diagonal for any edge length!") # Prints an introductory message explaining the purpose of the program.
iput = int(input("Please enter the edge length of your cube: ")) # Asks the user to input the edge length and converts it into an integer.
d = iput * m.sqrt(3) 
# Multiplies the user input value, which is stored in the variable 'iput', to the square root of 3. The result is stored in the variale 'd'
# Calculates the inner diagonal of the cube using the formula: diagonal = edge length * sqrt(3).
print("The length of the inner diagonal of a cube with the side length of  %.f is: %.2f" % (iput ,d))
# Prints the result using formatted string placeholders:
# %.f -> Represents the whole number value of `iput`
# %.2f -> Represents `d` rounded to 2 decimal places.

#### Part 3: Making change in coins ####
"""
  Author : Omer Khan
  Student Number : 753619
  Revison date : 1 March 2025
  Program : Even or Odd
  Description : A program that makes change for amounts less than $1.00 using the fewest coins.
VARIABLE DICTIONARY
  c(int) = Stores the user-inputted amount of change in cents. This value is updated throughout the program as coins are counted.
  q(int) = Stores the number of quarters (25 cents) in the given amount of change.
  d(int) = Stores the number of dimes (10 cents) in the remaining amount after quarters are removed.
  n(int) = Stores the number of nickel (10 cents) in the remaining amount after quarters are removed.
  p(int) = Stores the number of pennies (1 cent) left after removing all other coins.
"""
 
c = int(input("Please enter the amount of change in cents: "))  
# Asks the user to input the amount of change in cents and converts it into an integer. 
# The user input will be stored in the variable 'c'
q = c // 25
# Calculates the number of quarters (25 cents) in 'c' by performing integer division.  
# The result is stored in 'q', which represents the count of quarters.  
c %= 25  
# 'c' is updated to hold the remaining cents after quarters are taken out.  
#Checks the remainder
d = c // 10  
# Calculates the number of dimes (10 cents) in the remaining value of 'c'. 
# Result is stored in 'd', which represents the count of dimes.  
c %= 10  
# 'c' is updated to hold the remaining cents after dimes are taken out.  
#Checks the remainder
n = c // 5  
# Calculates the number of dimes (10 cents) in the remaining value of 'c'. 
# Result is stored in 'n', which represents the count of nickels.  
c %= 5  
# 'c' is updated to hold the remaining cents after dimes are taken out. 
#Checks the remainder
p = c  
# Since pennies are worth 1 cent, the resulting value of 'c' is stored in to 'p' (pennies)
# The following if statements check if each type of coin is used, then it will print the result accordingly.
if q > 0: #
    if q == 1:
        print(" Number of quarter %d: " % q, end = "")
        # If there is exactly 1 quarter, it prints "Number of quarter" (singular). 
    else:
        print(" Number of quarters: %d" % q, end = "")
        # If there is more than 1 quarter, it prints "Number of quarters" (plural). 

if d > 0:
    if d == 1:
        print(" Number of dime: %d" % d, end = "")
        # If there is exactly 1 dime, it prints "Number of dime" (singular).
    else:
        print(" Number of dimes: %d" % d, end = "")
        # If there is more than 1 dime, it prints "Number of dimes" (plural).

if n > 0:
    if n == 1:
        print(" Number of nickel: %d" % n, end = "" )
        # If there is exactly 1 nickel, it prints "Number of nickel" (singular).
    else:
        print(" Number of nickels: %d" % n, end = "")
        # If there is more than one nickel, it prints "Number of nickels" (plural).

if p > 0:
    if p == 1:
        print(" Number of penny: %d" % p, end = "")
        # If only 1 cent it will print "Number of penny"
    else:
        print(" Number of pennies: %d" % p ,end = "")
        #If more than once cent it will print "Number of pennies"
print(".") #adds a period at the end of the final statement. 

   
