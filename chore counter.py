chore = 5
n = 1
print ("task 1 - Make your bed. ")
print ("task 2 - Clean your room. ")
print ("task 3 - Wash the dishes. ")
print ("task 4 - Do your homework. ")
print ("task 5 - Mow the lawn. ")
completed = 0
while n <= chore:
 if n == 1 :
  task = "Make your bed"
 elif n == 2 :
  task = "Clean your room"
 elif n == 3 :
  task = "Wash the dishes"
 elif n == 4 :
  task = "Do your homework"
 else : 
  task = "Mow the lawn"
 chores = input(f"did you complete {task} (Yes or No) : ")
 if chores == "yes":
  n += 1
  completed += 1
  print ("Now it's time for your next chore.")
 else : 
  print ("Complete your chore and come back.")
 print ("you have", chore  - completed, "chores left.")
 
