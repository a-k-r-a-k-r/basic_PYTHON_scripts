#dont give the filename for this program as calendar
#it will give the error " Module 'calendar' has no 'month' member "

import calendar
year=int(input("Enter the year: "))
if calendar.isleap(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")