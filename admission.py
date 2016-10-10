number_of_registra = int(input().strip())

registration_info = dict()
for _ in range(number_of_registra):
    info = input().strip().split(', ')
    for subject in info[1:]:
        if subject in registration_info.keys():
            hold = registration_info[subject]
            hold.append(info[0])
        else:
            registration_info[subject] = [info[0]]

subject_keys = input().strip().split(', ')
for e in subject_keys:
    value = registration_info[e] if e in registration_info else ['Not found']

    print(e, ' -> ', ', '.join(value))
