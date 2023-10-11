def floatInput(varName, message):
    messageString = f'{message}: '
    globals()[varName] = float(input(messageString))
    print(f'Okay wir haben {varName} = {globals()[varName]} festgelegt.')

while True:

    print("Gibt's was zu rechnen?")

    floatInput('firstNo', 'Gib deine erste Zahl ein')
    floatInput('secondNo', 'Gib deine zweite Zahl ein')

    # firstNo = float(input("Erste Zahl: "))
    # print("Erste Zahl ist ", firstNo)

    # secondNo = float(input("Zweite Zahl: "))
    # print("Erste Zahl ist ", secondNo)

    operation = int(input("[1] Willst du addieren, dann tippe 1. \n[2] Willst du multiplizieren, dann tippe 2.\n[3] Willst du subtrahieren, dann tippe 3.\n[4] Willst du dividieren, dann tippe 4: "))


    if type(operation) == int  and 1 < operation < 5:
        print("Guti wir rechnen.")

    else:
        print("Du sollst 1, 2, 3 oder 4 eingeben du Lappen")

    if operation == 1:
        resultNo = firstNo + secondNo
        resultStr = f'{firstNo} + {secondNo} = {resultNo}' 

    elif operation == 2:
        resultNo = firstNo * secondNo
        resultStr = f'{firstNo} * {secondNo} = {resultNo}' 

    elif operation == 3:
        resultNo = firstNo - secondNo
        resultStr = f'{firstNo} - {secondNo} = {resultNo}' 

    elif operation == 4:
        if int(secondNo) != 0:
            resultNo = firstNo / secondNo
            resultStr = f'{firstNo} / {secondNo} = {resultNo}'
        else:
            print("Durch 0 teilen. Cool.")
            continue
             

    print("Hier: \n ", resultStr, "\nkann das sein?")