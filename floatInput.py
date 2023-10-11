def floatInput(varName, message):
    messageString = f'{message}: '
    globals()[varName] = float(input(messageString))
    print(f'Okay wir haben {varName} = {globals()[varName]} festgelegt.')

floatInput('firstNo', 'Gib deine erste Zahl ein')