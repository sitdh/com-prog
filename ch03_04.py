(day, month, year) = input().strip().split()

day = int(day); month = int(month); year = int(year)

if month < 3:
    month += 12
    year -= 1

c = year / 100
k = year % 100

day + 26 * (m + 1) / 10 + k + k/4

week_day_name = ''

# 1. Follow from flowchart
if 0 == week_day:
    week_day_name = 'SAT'
elif 1 == week_day:
    week_day_name = 'SUN'
elif 2 == week_day:
    week_day_name = 'MON'
elif 3 == week_day:
    week_day_name = 'TUE'
elif 4 == week_day:
    week_day_name = 'WED'
elif 5 == week_day:
    week_day_name = 'THU'
elif 6 == week_day:
    week_day_name = 'FRI'

print(week_day_name)

# 2. SHORTER VERSION
# week_day_list = ['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI']
# print(week_day_list[week_day])
