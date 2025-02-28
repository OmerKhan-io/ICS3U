print("Welcome to the even and odd detector!")
num1 = int(input("Enter your first number"))
num2 = int(input("Enter your second number"))

if (num1 % 2 == 0 and num2 % 2 == 0):
  print("The product of both numbers are even")
elif(num1 % 2 == 1 and num2 % 2 == 1):
  print("The product of both numbers are odd")
elif(num1 % 2 == 1 and num2 % 2 ==0):
  print("The product of both numbers are even ")
else:
  print("The product of both numbers are even ")

Part 2

import math
print("I will find the cube's inner diagonal for any edge length!") 
iput = int(input("Please enter the edge length of your cube: "))

d = iput * math.sqrt(3)
print("The length of the inner diagonal of a cube with the side length of  %.f is: %.2f" % (iput ,d))

#Part 3

import math 
c = int(input("Please enter the amount of change in cents: "))
q = 0
n = 0
d = 0
p = 0
cents = 0
change = 0

if c >= 100:
   change = change % 100

if c >= 25:
   q = c // 25
   change = c % 25
   print("Number of quarters %d: " % q, end = "")

if c >= 10:
   d = c//10
   change = c % 10
   print("Number of quarters %d: " % d, end = "")
  
if c >= 5:
   n = c//5
   change = c%5
   print("Number of quarters %d: " % n, end = "")
   

   
