number_of_data = int(input().strip())

ma = [0] * number_of_data
numbers = [int(c) for c in input().strip().split()]

for i in range(1, number_of_data - 1):
    ma[i] = (sum(numbers[i-1:i+2])/3)

ma[0] = sum(numbers[0:2])/2
ma[-1] = sum(numbers[number_of_data - 2:])/2

ma = [str(d) for d in ma]
print("\n".join(ma))
