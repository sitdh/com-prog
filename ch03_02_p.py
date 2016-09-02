number_of_input = int(input())
summation = 0

if 0 == number_of_input:
    print('No Data')
    exit()

else:
    for _ in range(0, number_of_input):
        summation += float(input())

    print(summation / number_of_input)
