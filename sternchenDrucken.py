#ohnespaces

for i in range(7, 0, -2):
    while i > 0:
        print('*', end='')
        i -= 1
    else:
        print()

#mit spaces aber keine einzelnen zeichen. mit einzelnen zeichen fuer spaces ist nervig wie sau und streng genommen nicht aufgabenstellung alla

for i in range(7, 0, -2):
    print(' ' * ((7 - i) // 2), end='')
    print('*' * i, end='')
    print(' ' * ((7 - i) // 2))
    print()