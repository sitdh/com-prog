# -- Long version -- 
# numbers = input().strip()
# numbers = [int(number) for number in numbers]
# 
#### 
# -- Short version --
numbers = [int(number) for number in input().strip().split()]

maximum_number = numbers[0]
for i in range(6):
    maximum_number = numbers[i] if maximum_number < numbers[i] else maximum_number 

print(maximum_number)
