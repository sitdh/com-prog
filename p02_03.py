first_word = [c for c in input().strip()]
second_word = [c for c in input().strip()]

list_of_numbers = 'abcdefghijklmnopqrstuvwxyz' 
list_of_numbers = list_of_numbers + list_of_numbers.upper()

remain_char = set(first_word).intersection(set(second_word))

printed_char = [];
for c in list_of_numbers:
    if c in remain_char:
        printed_char.append(c)
        remain_char.discard(c)

p = ' '.join(printed_char) if len(printed_char) else 'NONE'
print(p)
