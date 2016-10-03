# receive B.E. and convert to A.D.
year = int(input().strip()) - 543 

days_in_feb = 28
if (0 == year % 4) and (0 != year % 100):
    days_in_feb += 1

print(days_in_feb)
