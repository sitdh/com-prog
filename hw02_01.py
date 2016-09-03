import math

a = float(input())
b = float(input())
c = float(input())

if 0 == a and (b**2 <= 4*a*c):
    exit()

first_answer    = ((-1 * b) + math.sqrt((b ** 2) - 4 * a * c)) / ( 2 * a )
second_answer   = ((-1 * b) - math.sqrt((b ** 2) - 4 * a * c)) / ( 2 * a )

print(first_answer, second_answer)
