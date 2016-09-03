number = int(input())

powers = ''

for p in range(1, 6):
    powers += str( number ** p ) + " "

print( powers.strip() )
