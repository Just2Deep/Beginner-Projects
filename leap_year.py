# Finding leap year

def LeapYear(year):
    return year % 4 == 0 and (year % 100 == 0 or year % 400 != 0)


print(LeapYear(2002))
