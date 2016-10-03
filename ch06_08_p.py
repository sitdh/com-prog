data = 'abcdefghijklmnopqrstuvwxyz' 
data = data.upper() + data
data = '0123456789' + data

count_info = [0] * len(data)

input_string = input().strip()

for c in input_string:
    i = data.index(c)
    if (c in data) and (i >= 0):
        count_info[i] += 1

count_info = [str(c) for c in count_info]
print(' '.join(count_info))
