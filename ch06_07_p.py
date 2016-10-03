months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

month, day, year = input().strip().split("/")
print("%s %s %s" % (day, months[int(month) - 1], year))

