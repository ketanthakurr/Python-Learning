n = int(input("Enter the Value : "))
ans = 1 
while ( n > 9):
    n = n // 10
    ans = ans + 1
print(ans)