bmi = ''

while True:

    input_numbers = input()

    if ( '-1' == input_numbers ) or ( -1 == input_numbers.find(' ') ):
        break

    input_numbers = input_numbers.split()
    weight = int(input_numbers[0])
    height = int(input_numbers[1])

    tmp = weight / ( height / 100 ) ** 2

    bmi += str(tmp) + "\n"

print(bmi.strip())
