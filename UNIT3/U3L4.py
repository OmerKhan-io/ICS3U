ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
for i in range(len(ar2)):
  ar3 = ar2[i]
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
      # Prints each number on the same line row
  print() # PREDICT A
  # Carrige return; moves to next line

print(ar2) # PREDICT B
#Prints the exactly what is stored in the array, including the 2 brackets on each end
sum=0
arr32 = []
for j in range(3):
  for x in range(5):
    sum += int(ar2[j][x])
  arr32.append(sum)
  print(arr32)
#modifey

ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]

add = 0
ar32 = []

for j in range (3): #Rows
  for i in range(5): #Columns
    add = add + ar2[j][i]
  ar32.append(add)
  add = 0
print(ar32)
