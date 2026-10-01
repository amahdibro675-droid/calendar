import calendar
 
## input year and month from the user
year = int(input("ENTER YEAR: "))
month = int(input("ENTER MONTH: "))

## return the output
print("\n", calendar.month(year,month))