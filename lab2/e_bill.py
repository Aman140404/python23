id = int((input("enter your coustomer ID=>")))
name = input("please enter your name as registered=>")
unit = float(input("entere the number of units consumed=>"))
if unit <= 199:
    amt = 1.20*unit
elif unit >= 200 and unit < 400:
    amt = 238.8+(unit-199)*1.50
elif unit >= 400 and unit < 600:
    amt = 238.8+300+(unit-399)*1.80
else:
    amt = 898.8+(unit-599)*2
if amt > 400:
    total = amt+(0.15*amt)
elif amt < 100:
    total = 100
else:
    total = amt
print("\t\tELECTRICITY BOARD OFFICE")
print("Dear")
print("name=>", name)
print("ID=>", id)
print("your electricity bill for consumption of ",
      unit, "units of electricity is=>")
print("total=", total, "/-rupees only")
