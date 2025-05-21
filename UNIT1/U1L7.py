# I predict that it would ask the user for the x and y value, then it will check if there have a common factor. 
# If it does it will print the value of x and y, if the don't have a common factor, it will not print the final print statement. In this case, it will stop at the Yes! 3 is a factor of 6


import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)


#modify 1 and 2 again
import math
x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = 0
if y!=0:
  rem = x % y
  if rem == 0: 
    print("Yes!", y, "is a factor of", x)
  else:
    print("No!", y, "is not a factor of", x)
else:
  print("Do not enter a zero")

#modify 3
# I predict that it would ask the user for the x and y value, then it will check if there have a common factor. If it does it will print the value of x and y, if the don't have a common factor 
import math

x = input("Please input a whole number between 1 and 20: ")
x = int(x)
y = input("Please input another whole number between 1 and 20: ")
y = int(y)
if (x >= 0) and (x <= 20):
  print( x, "is between 1 and 20")
else: 
  print("No!", x, "is out of range")
if (y >= 0) and (y <= 20):
  print(x, "is between 1 and 20")
else: 
  print("No!", y, "is out of range")
rem = x % y
if rem ==0:
    print("Yes!", y, "is a factor of", x)
else:
      print(y, "is not a factor of", x)
