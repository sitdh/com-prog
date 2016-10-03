(number_of_data, needle) = [int(x) for x in input().strip().split()]

f = 0
for _ in range(number_of_data):
    number = int(input().strip())
    if number == needle:
        f += 1

print(f)
