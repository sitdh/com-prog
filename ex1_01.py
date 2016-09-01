import math

x = float(input())

prop_2 = -1 * (x**2) / math.factorial(2)

prop_3 = (x**4) / math.factorial(4)

prop_4 = -1 * (x**6) / math.factorial(6)

cos_x = float(1 + prop_2 + prop_3 + prop_4)

print(prop_2)
print(prop_3)
print(prop_4)
print(cos_x)
