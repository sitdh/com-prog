first_number = int(input())

if 1 >= int(first_number):
    print('none')
    exit()

prime_count = '' 

while True:

    if 2 == first_number:
        prime_count += ' 2'
        break

    running_number = first_number
    divider = first_number // 2 if ( 0 == first_number % 2 ) else ( first_number // 2 ) + 1;
    count = 0

    while divider != 1:
        if 0 == running_number % divider:
            count += 1

        divider -= 1

    if count == 0:
        prime_count += ' ' + str( running_number )

    first_number -= 1
    if 1 == first_number:
        break

p = ''
for c in prime_count.strip().split():
    p = c + ' ' + p
print( p.strip() )
