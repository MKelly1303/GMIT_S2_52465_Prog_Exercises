# Greatest Common Divisor
# While Loop Review
# Mark Kelly

a = 50
b = 20

#One way would be...
#while b>0:
#  tmp = a
#  a = b
#  b = tmp % b

while b>0:
  a, b = b, a % b
#this way is neater 

# '% = Modulus	Remainder when a is divided by b

print(a)