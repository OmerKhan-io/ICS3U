# I predict that the function will add two numbers and then the will be printed outside the function
def add(a: float, b: float) -> float:
   sum = a + b
   return sum
sum = add(7.0, 2.0)
print(sum) #this will print output as a float data type

#Modify 1

def add(a: float, b: float) -> float:
   sum = a + b
   return sum
sum = add(7.0, 2.0)
print(isinstance(sum, float)) #this will print output as a float data type
#is isinstance is a boolean


#Modify 2
def a_abs (a):
  if a < 0:
    return -a
  else:
    return a
    
print(abs(-5.2))


