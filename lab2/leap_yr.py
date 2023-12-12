year = int(input("enter a year to check"))

if year % 400 == 0 and year % 100 == 0:
    print("the year", year, "is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("the year", year, "is a leap year")
else:
    print("the year", year, "is not a leap year")
