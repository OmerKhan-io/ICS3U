import math
n = int(input("Enter a number: "))
def factorize(n):
 square_root = math.sqrt(n)
 limit = math.floor(square_root)
 factors = []
 for j in range (1, limit + 1):
  if n % j == 0:
    factors.append(j)
 return factors

print("Factors of the number:", factorize(n))

def total(n):
  total = 0
  for i in n:
    total += n
    if total > n: 
      print("%d is an abundant number", n)
    elif total < n:
      print("%d is a deficient number", n)
    elif total == n:
      print("%d is a proper number", n)
  print("Goodbye!")
  
print(total(factorize(n)))



------------------
import math

n = int(input("Enter a number: "))

def factorize(n):
    square_root = math.sqrt(n)
    limit = math.floor(square_root)
    factors = []
    for j in range(1, limit + 1):
        if n % j == 0:
            factors.append(j)
            if j != n // j and n // j != n:
                factors.append(n // j)
    return factors

factors = factorize(n)
print("Factors of the number:", sorted(factors))

def classify_number(n, factors):
    # Sum of proper divisors (excluding n itself)
    total_divisors = sum(factors) - n
    if total_divisors > n:
        print(f"{n} is an abundant number.")
    elif total_divisors < n:
        print(f"{n} is a deficient number.")
    else:
        print(f"{n} is a perfect number.")

classify_number(n, factors)
print("Goodbye!")
