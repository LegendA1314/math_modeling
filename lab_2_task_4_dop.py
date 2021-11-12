a = int(input('Введите свое число '))

while a > 1:

    i = 2
    f = 0
    while 1:

        if a % i == 0:
            a = a // i
            print(i)
            f = 1
            break
        else:
            i += 1

    if f == 1:
        continue
print()