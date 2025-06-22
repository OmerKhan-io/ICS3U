ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
for i in range(len(ar2)):
  ar3 = ar2[i]
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
  print() # PREDICT A 
#Prints the values of each row printed in each line follow by spaces after each character

print(ar2) # PREDICT B
#Prints the entire 2-D array as a list of list, exactly how it was stored in Python


# Modify 
ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
sum_list = [] # This will store total number of each row "scores"
              # One at a time
sum_lists = []
for i in range(len(ar2)):
  #The len for the array is 3, so it will 
  ar3 = ar2[i]
  sum_list = sum(ar3)
  sum_lists.append(sum_list)
  

for x in range(len(sum_lists)):
  if x < len(sum_lists)-1:
      print(sum_lists[x], end=", ")
  else:
      print(sum_lists[x])
  
