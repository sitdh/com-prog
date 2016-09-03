number_list = input().strip()

minus_position = number_list.find('-1')

if -1 == number_list.find('-1'):
    exit()

number_list = number_list[:minus_position].strip().split()

summation = 0

for number in number_list:
    summation += int(number) 

print(summation / len(number_list))
