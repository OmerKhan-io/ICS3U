total = 0 
f_total = 1
user = int(input("Give me a value: "))
print("Counting from j = 1 to %d" % user )
print("  j   tri      factorial")
for j in range(1,user+1):
  total += j
  f_total *= j
  print("%5d %5d %9d" % (j, total, f_total))
  
