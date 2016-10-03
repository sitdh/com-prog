n = int(input().strip()) 
data_list = list()

while n > 0:
    data_list.append(n)
    n = int(input().strip())

threshold = len(data_list) // 2 if len(data_list) % 2 == 0 else 1 + (len(data_list) // 2)

freq = [0] * len(data_list)
for (i, e) in enumerate(data_list):
    for el in data_list:
        if e == el:
            freq[i] += 1

data = list()
if max(freq) < threshold:
    print('Not found')

else:
    for (i, e) in enumerate(freq):
        if e >= threshold:
            data.append(data_list[i])

answer = list()
for e in data:
    if e not in answer:
        answer.append(e)
answer.sort()
print(' '.join([str(q) for q in answer]))
