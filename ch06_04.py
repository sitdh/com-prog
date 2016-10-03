number_of_data = int(input().strip())

data_list = list()
for _ in range(number_of_data):
    data_list.append(int(input().strip()))

freq_data = [0] * number_of_data
for (i, e) in enumerate(data_list):
    for el in data_list:
        if e == el:
            freq_data[i] += 1

max_frequency = max(freq_data)

maximum_list = list()
for (i,e) in enumerate(freq_data):
    if e == max_frequency:
        maximum_list.append(data_list[i])

print(min(maximum_list))
