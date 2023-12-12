def days(d,m,y,dd,mm,yyyy):
    """date=int(input("enter your birth date (DD)"))
    month=int(input("enter your birth month"))
    year=int(input("enter your birth year"))"""
    day=0
    for i in range(y,yyyy+1):
        if year % 400 == 0 and year % 100 == 0:
            day=day+1
        elif year % 4 == 0 and year % 100 != 0:
            day=day+1
        else:
            day=day+0
    days=day+(y-yyyy)*365
