print ("========================================")
print ("         Custom Ride calculator         ")
print ("========================================")
print ("vehicle number 1 is : An Aeroplane")
print ("vehicle number 2 is : A car")
print ("vehicle number 3 is : A Scooter")

vehicle = int(input("Do you want to choose vehicles 1, 2, or 3?:"))


if vehicle == 1:
 detail = int(input("Do you want a 1. a Public plane, or 2. a Private plane"))
 if detail == 1:
   print ("You have chosen a public aeroplane.")
   print ("This is a very cost-effective choice")
 elif detail == 2:
   print ("You have chosen a private aeroplane.")
   print ("This is a quite expensive choice.")
 else:
   print("please choose 1 or 2")

elif vehicle == 2:
 detail = int(input("Do you want 1. a BMW, or 2. a Hundai"))
 if detail == 1:
   print ("You have chosen a BMW.")
   print ("This is a very fancy choice")
 elif detail == 2:
   print ("You have chosen a Hundai.")
   print ("This is a classic.")
 else:
   print("please choose 1 or 2")


elif vehicle == 3:
 detail = int(input("Do you want 1. a scooter, or 2. a motorcycle"))
 if detail == 1:
    print ("You have chosen a scooter.")
    print ("This is a perfect choice for shopping.")
 elif detail == 2:
    print ("You have chosen a motorcycle.")
    print ("This is a good choice if you are in a rush.")
 else:
    print("please choose 1 or 2")

else:
  print ("Please choose either 1, 2, or 3.")












