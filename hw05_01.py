number_of_data = int(input().strip())

data = list()

for _ in range(number_of_data):
    data.append(int(input().strip()))

# mean
mean = sum(data) / number_of_data
data = sorted(data)

# median
median = 0
if 1 == len(data) % 2:
    median = data[(len(data) // 2)]
else:
    median = (data[(len(data) // 2) - 1] + data[len(data) // 2]) / 2


# mode 
count_list = [0] * len(data)

for i, d in enumerate(data):
    for e in data:
        if d == e:
            count_list[i] += 1

mode = data[count_list.index(max(count_list))]

print(mean, median, mode)
