number_of_data = int(input().strip())

raw_numbers = list()
for _ in range(number_of_data):
    raw_numbers.append(int(input().strip()))

number_sorted = False
# Bubble sort
while not number_sorted:
    number_sorted = True
    for i in range(0, number_of_data-1):
        if raw_numbers[i] < raw_numbers[i+1]:
            number_sorted = False
            hold = raw_numbers[i+1]
            raw_numbers[i+1] = raw_numbers[i]
            raw_numbers[i] = hold

raw_numbers = [str(n) for n in raw_numbers]
print(' '.join(raw_numbers))
