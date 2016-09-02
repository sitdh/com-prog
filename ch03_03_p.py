summation = 0
input_number = float(input()) 
number_of_input = 0

while input_number != -1:
    number_of_input += 1
    summation += input_number
    input_number = float(input())

if 0 == number_of_input:
    print("No Data")
else:
    print(summation / number_of_input)
