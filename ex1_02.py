first_card  = input().strip().upper()
second_card = input().strip().upper()
third_card  = input().strip().upper()

total_point = 0

if first_card == 'A':
    total_point += 1
elif first_card in 'JQK':
    total_point += 10
else:
    total_point += int(first_card)

if second_card == 'A':
    total_point += 1
elif second_card in 'JQK':
    total_point += 10
else:
    total_point += int(second_card)

if third_card == 'A':
    total_point += 1
elif third_card in 'JQK':
    total_point += 10
else:
    total_point += int(third_card)

if total_point < 17:
    print('hit')
elif total_point > 21:
    print('bust')
else:
    print('stand')
