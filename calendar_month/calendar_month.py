#dont give the filename for this program as calendar
#it will give the error " Module 'calendar' has no 'month' member "

import calendar
year=int(input("Enter the year: "))
month=int(input("Enter the month(1-12): "))
print (calendar.month(year,month))