from datetime import date
birth_date = date(2004, 12, 12)
today = date.today()
age_in_days = (today - birth_date).days
print(f"Your age in days: {age_in_days}")
