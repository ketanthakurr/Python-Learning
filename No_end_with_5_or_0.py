print("Enter your no.: ")
a = int(input())
if (a%5 == 0):
    if (a%10 == 0):
        print("No. ends with 0")
    
    else:
        print("No. ends with 5")
else:   
    print("Other")