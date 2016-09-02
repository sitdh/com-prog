number = int(input())

divider = number // 2

numbers = ''

while divider != 1:
    if 0 == number % divider:
        numbers += " " + str(divider)

    divider -= 1

if 0 == len(numbers):
    print('Prime Number')
else:
    print(numbers[1:])
