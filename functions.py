# Greatest Common Divisor
# Using Functions
# Mark Kelly

# Defining 2 user inputted integers
a = int(input("Please enter an integer: "))
b = int(input("Please enter a 2nd integer: "))

def gcd(a, b):
  """
  returns the greatest common divisor of a and b
  """
  while b>0:
    a, b = b, a % b
  return a

# '% = Modulus	Remainder when a is divided by b

#print(gcd(20, 50))
print(f'The greatest common divisor of {a} and {b} is: ', gcd(a, b))