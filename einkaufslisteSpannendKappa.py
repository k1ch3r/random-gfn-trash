operationArray = ['Liste anschauen', 'Etwas auf die Liste schreiben', 'Etwas von der Liste entfernen', 'Programm abballern alla!']

def stringifyArray(arrayName):
    return '\n'.join([f'[{index}]: {operation}' for index, operation in enumerate(arrayName)])

def addItem(itemName):
    shoppingListArray.append(itemName)

def removeItem(itemIndex):
    shoppingListArray.pop(itemIndex)

operationsString = stringifyArray(operationArray)

menuString = f'Willst du:\n' + operationsString + '\nGib jetzt die entsprechende Zahl ein: '

currentInputOperation = 0

# in funktionen beinhaltete sachen als argumente verwenden hilft gegen unuebersichtliche gliederung. also gedanken ueber argumente und funktionen machen und definitione ausserhalb vermeiden evtl oefter ne option an die ich nicht denke?!

def chooseOperation():
    global currentInputOperation
    try:
        currentInputOperation = int(input(menuString))
        print("Gewählte Option:", operationArray[currentInputOperation])
    except ValueError:
        print('servuus ich bin ein value error. mein array weiss nicht welche zahl du eingeben willst.')
    except IndexError:
        print('hallo ich bin ein index error. die zahl steht nicht im array brudi.')

# keine ahnung wann ich catch alls und wann spezifische exceptions brauche tbh aber ist eh nur ein unsinniges spassprojekt.

shoppingListArray = ['nichts', 'leer']
shoppingListString = stringifyArray(shoppingListArray)

print('Hallo. Weil eine Einkaufsliste als Python Terminal App super spannend und sinnvoll ist kannst du hier Sachen in eine Liste packen und dir die anschauen.\n')

print('Hier ist deine aktuelle Liste:')
print(stringifyArray(shoppingListArray))

def menuLoop():
    while True:
        
        try:
            chooseOperation()
            if currentInputOperation == 0:
                print('Hier ist deine aktuelle Liste:')
                print(stringifyArray(shoppingListArray))
            elif currentInputOperation == 1:
                itemToAdd = input('Gib den Artikel zum aufschreiben ein: ')
                addItem(itemToAdd)
                print('Okay, ', itemToAdd, ' wurde aufgeschrieben.')
            elif currentInputOperation == 2:
                itemToRemoveIndex = int(input('Gib die Nummer des Artikels ein, den du entfernen willst: '))
                itemToRemoveName = shoppingListArray[itemToRemoveIndex]
                removeItem(itemToRemoveIndex)
                print('Okay, ', itemToRemoveName, ' wurde entfernt.')
            elif currentInputOperation == 3:
                print('schade brudi werd dich vermissen hdgdl baaaaaii')
                break
        except KeyboardInterrupt:
            print('Ctrl + C macht programm aus. Nerd.')
            break 
        except:
            print('AU WEIA! du liest mein catch all.')
            break
            
menuLoop()