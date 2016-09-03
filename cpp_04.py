first_number = int(input())
second_number = int(input())

large_number = max(first_number, second_number)
small_number = min(first_number, second_number)

remaining_number = 0

gcd = 0

while True:
    times = large_number // small_number

    remain = large_number - ( small_number * times )

    if 0 == remain:
        gcd = small_number
        break
    else:
        large_number = small_number
        small_number = remain

print(gcd)
