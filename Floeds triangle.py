r = int (input ("Give the number of rows : "))
number = 0
for n in range ( 1, r + 1):
    for m in range ( 1, n + 1):
        number += 1
        print (number, end = "")
    print ()