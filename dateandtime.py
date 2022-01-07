from datetime import datetime
 
my_string = str(input('Enter date(yyyy-mm-dd hh:mm): '))
my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M")
 
print(my_date)
