num = int(input())
fact = 1
if (num < 1):
    print('Not Defined')
else:
    while(num > 0):
        fact = fact * num
        num = num - 1
    print(fact)