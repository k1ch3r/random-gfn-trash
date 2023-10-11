def moduloMustermaler(x, y):
    ausgabestring = ''
    i = 1
    for i in range(x, y):
        if i % 6 == 0:
            ausgabestring = ausgabestring + "|"
        else:
            ausgabestring = ausgabestring + '-'
    print(ausgabestring)

moduloMustermaler(1, 24)