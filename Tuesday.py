import datetime
today = datetime.datetime.today()
dayofweek = today.weekday()

print("lets check if it's Tuesday")

if dayofweek == 1:
  print("It's Tuesday!")
elif dayofweek == 0:
  print("It will be Tuesday tomorrow")
elif dayofweek ==2:
  print("Ah, it was Tuesday yesterday!")
else:
  print("Sorry, it's not Tuesday")


print("Thanks for checking!")