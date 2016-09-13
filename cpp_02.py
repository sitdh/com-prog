number = int(input())

if 1 >= number:
    exit()

while True:
    divider = number // 2 if 0 == number % 2 else number // 2 + 1 ;

    while divider > 1:
        if 0 == number % divider:
            pass
