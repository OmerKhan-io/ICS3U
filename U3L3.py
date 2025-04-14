items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
for i in range(len(items)): # Predict A: State the purpose,
# Cycles through each values in the array
#Data types in Strings
#no nothing is printed yet
                           
    sizeI = len(items[i]) #size 
    sizes.append(sizeI)

for i in range(len(sizes)): # Predict B: State the output
    print("%d %s" % (sizes[i], items[i]))
    # Prints out each item in order with the number of characters (size) for each
    if len(items[i]) == sizes[i]:
      print("True")
    else:
      print("False")
    
