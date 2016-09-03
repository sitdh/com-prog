number = int(input())

total = 0
for i in range(1, number + 1):
    if 0 == i % 3 or 0 == i % 5:
        total += i
else:
    print(total)
