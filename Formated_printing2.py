'''
num = int(input())
for i in range(1, 11):
    print(num, 'X', i, '=',num * i)
    #print(f'{num} X {i} = {num * i}')
    # We used formated printing insted of writing quotes for string we used the quots 1 time for strings
    # And used brackets we don't want to be in strings
'''
'''
pi = 22 / 7
print(f'Value of Pi is = {pi}')
print(f'Value of Pi is = {pi:.2f}') # Used ':.2f' to write the only 2 valus after the '3.'
'''
'''
print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))
# Used :5d to print the same output from opposite side:
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))
'''
