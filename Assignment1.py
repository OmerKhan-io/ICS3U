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
 
c = int(input("Please enter the amount of change in cents: "))  

q = c // 25  
c %= 25  

d = c // 10  
c %= 10  

n = c // 5  
c %= 5  

p = c  

if q > 0:
    if q == 1:
        print(" Number of quarter %d: " % q, end = "")
    else:
        print(" Number of quarters: %d" % q, end = "")

if d > 0:
    if d == 1:
        print(" Number of dime: %d" % d, end = "")
    else:
        print(" Number of dimes: %d" % d, end = "")

if n > 0:
    if n == 1:
        print(" Number of nickel: %d" % n, end = "" )
    else:
        print(" Number of nickels: %d" % n, end = "")

if p > 0:
    if p == 1:
        print(" Number of penny: %d" % p, end = "")
    else:
        print(" Number of pennies: %d" % p ,end = "")

   
