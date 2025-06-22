items = ["Apples", "Bananas", "Cherries", "Dosa"]
print(items) 
# Predict A - Does this really print anything?
#It prints ['Apples', 'Bananas', 'Cherries', 'Dosa']
#with single quotatiuon marks

print("The number of items is %d." % len(items)) 
# Predict B
# The number of items are 4, each seperated by quotation marks and comma

for i in items: 
# Predict C
# This will print each item such as "Apples", each time
    print(i)

for c in range(len(items)): 
# Prediction D
# This will print each item such as "Apples", each time
#Similar function as prediction C, but this is a diffirent approach, which call the index. 
    print(c, items[c])

# Modify 

Itemlist = int(input("Enter number of items"))
Arr = []
for i in range(Itemlist):
  item = input("Enter an item: ")
  Arr.append(item)

Arrlen = len(Arr) #checks length of the item array
print("You have %d items" % Arrlen)

for x in Arr:#prints each item of the array 
  print(x)

