def operateMath(operation):
    while True:
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