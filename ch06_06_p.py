count_number = [0] * 10

digits = input().strip()

for digit in digits:
    if digit.isnumeric():
        count_number[int(digit)] += 1

print("\n".join([str(i) for i in count_number]))
