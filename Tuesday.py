import datetime
today = datetime.datetime.today()
dayofweek = today.weekday()

if dayofweek == 2:
  print("It's Tuesday!")
else:
  print("Sorry, it's not Tuesday")