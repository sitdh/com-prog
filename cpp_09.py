first_number = int(input())

prime_count = 0

while True:

    if 1>= first_number:
        break

    running_number = first_number
    divider = first_number // 2 if ( 0 == first_number % 2 ) else ( first_number // 2 ) + 1;
    count = 0

    while divider != 1:
        if 0 == running_number % divider:
            count += 1

        divider -= 1

    if count == 0:
        prime_count += 1

    first_number -= 1
    if 1 == first_number:
        break

print(prime_count)
