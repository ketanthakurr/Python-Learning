print(" Enter Time ")
time = int(input())
longer = int(input())
if (time >= longer):
    price = int(input())
    Higher = int(input())
    if (price>=Higher) :
        print("train")
    else:
        print("Coach")
else:
    price = int(input('Enter Price: '))
    Higher = int(input('Define Higher'))
    if( price>=Higher):
        print('Day time Flight')
    else:
        print('Night Flight')
print('Arrived to the city 2')