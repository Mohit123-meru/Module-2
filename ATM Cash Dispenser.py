p = True
hundred = 0
Fifty =  0
one = 0

while p == True:
    name = input("What is your name? : ")
    amount = int (input ("How much do you want to withrdraw? : "))
    if amount <= 0:
        print ("This number is invalid. Please re-enter a positive vaue. ")
        continue
    cost = 1
    remaining = amount
    while cost < 4:
        if cost == 1:
            value = 100
        elif cost == 2:
            value = 50
        else:
            value = 1
        count = remaining // value
        print (remaining - (value * count))
        remaining = remaining - value * count
        cost += 1
    customer = input ("Is there a customer? (Yes/No) : ")
    print ("Your transaction for today is complete!")
    if customer == "Yes":
        p = False
    elif customer == "no":
        print ("Bye!")
        break
      
















