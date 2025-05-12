def factorize(n):
 n = int(input("Enter a number: "))
 square_root = math.sqrt(n)
 n = math.floor(square_root)
for j in range (i,n):
  if n % j == 0:
    factors.append(j)
  return factors

print("Factors of the number:", factorize())

import math

def factorize():
    n = int(input("Enter a number: "))
    factors = []

    for j in range(1, n + 1):
        if n % j == 0:
            factors.append(j)

    return factors

# Call the function and print the factors
print("Factors of the number:", factorize())
