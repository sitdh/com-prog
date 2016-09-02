start_hour      = int(input())
start_minute    = int(input())
stop_hour       = int(input())
stop_minute     = int(input())

hour_diff   = stop_hour - start_hour 
min_diff    = stop_minute - start_minute

parking_price = 0;

'''
Out of service
'''
if not(start_hour in range(7, 24) and stop_hour in range(7, 24)):
    exit(0)

'''
In the case of start_minute greater than stop_minute min_diff will be negative number
'''
if min_diff < 0 and hour_diff > 0:
    hour_diff -= 1
    min_diff += 60

if (min_diff > 15 and hour_diff == 0) or (min_diff > 0 and hour_diff > 0):
    hour_diff += 1

if hour_diff > 6: 
    parking_price = 200 

else:

    if hour_diff >= 4:
        parking_price += (hour_diff - 3) * 20
        hour_diff = 3

    if hour_diff <= 3:
        parking_price += hour_diff * 10

print(parking_price)
