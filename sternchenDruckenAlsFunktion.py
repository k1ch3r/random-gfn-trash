def sterneDrucken(rangeStart, rangeStop, rangeStep):
    for i in range(rangeStart, rangeStop, rangeStep):
        print(' ' * ((rangeStart - i) // 2), end='')
        print('*' * i, end='')
        print(' ' * ((rangeStart - i) // 2))
        print()

sterneDrucken(7, 0, -2)

sterneDrucken(40, 0, -1)