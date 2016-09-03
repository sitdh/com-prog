message = input()

vowel = 'aeiouAEIOU'
consonant = 'bcdfghjklmnpqrstvwxyz'
consonant += consonant.upper()

vowel_count = 0
consonant_count = 0

for c in message:
    if c in vowel:
        vowel_count += 1
    elif c in consonant:
        consonant_count += 1

print(vowel_count, consonant_count)
