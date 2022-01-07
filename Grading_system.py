print("Enter your marks : ")
marks = int(input())
if ( 100 >= marks >= 90):
    print("A Grade")
elif (80 <= marks < 90):
    print("B Grade")
elif (70 <= marks < 80):
    print("C Grade")
elif (60 <= marks < 70):
    print("D Grade")
elif (0 < marks <= 60 ) :
    print("E Grade")
else:
    print("Invalid Data")