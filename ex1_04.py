capital_string = input().upper().strip() + " "

character = capital_string[0]
number = 0

line_print = ''

for c in capital_string:

    if c != character:
        line_print += character + " " + str(number) + " "
        number = 0
        character = c

    number += 1

print(line_print.strip())
