"""
Shah soumil Nitin
Bachelor in Elecctronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

"""

# Define function to return true or false if its leap year

'''
There are three criteria to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
'''


def leayr(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False


value = int(input("Enter Year to check if its a leap year or not "))
# return value 
reply=leayr(value)

if reply== True:
    print ("{} is a leap year".format(value))
else:
    print("{} is not a leap Year".format(value))



