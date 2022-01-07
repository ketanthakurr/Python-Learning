num = int(input("Enter any no.:"))
fact = 1
if (num > 0):
    while ( num > 0 ):
        fact = fact * num
        num = num - 1
    print(fact)
else:
    print("Invalid no.")
