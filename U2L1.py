#I predict that it would display the 3 choices and then it will ask user to input his choice
#If A is chosen, it will print I prefer apples
#If B is chosen, it will print I prefer bannanas
#otherwise the only remaining option is, I prefer cherries

print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
else:
    print("I prefer cherries")
    
#Modify 1

print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif (ch == "C"):    
    ("I prefer cherries")
else:
    print("Error...")

# Modify 2

choice = int(input("Enter a number between 1 and 100"))

if (choice>=80) and (choice <=100):
  print("A")
elif (choice>=70) and (choice<=79):
  print("B")
elif (choice>=60) and(choice<=69):
  print("C")
elif (choice>=50) and (choice<=59):
  print("D")
elif (choice<50):
  print("F")
else:
  print("Not a valid number")
