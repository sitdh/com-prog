a = int(input())

if a < 0:
    a = a * (-1)

    summation = 0

    for number_char in str(a):
        summation += int(number_char)

    print(summation)

else:
    m = 2
    last = 2

    while True:

        ok = True
        k = 2

        while True:
            if 0 == m % k:
                ok = False
                break
            else:
                k += 1

                if k >= m:
                    break

        if ok:
            last = m

        m += 1

        if m >= a:
            break

    print(last)
