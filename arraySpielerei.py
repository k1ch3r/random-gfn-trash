# leeres array (python nent arrays list. ich nicht.)

testArray = []


# erweitern

testArray.append('Unsinn')
testArray.append('macht')
testArray.append('mir')
testArray.append('Spass')


# ganzes array anschauen
print(testArray)


# einzelnes element anschauen
print(f'das zweite element von testArray ist "{testArray[1]}"')


# element von hinten definieren
print(f'das letzte element von testArray ist "{testArray[-1]}"')


# extend methode

zweitesArray = ['mehr', 'buchstaben', 'zeichen', 'krams']
testArray.extend(zweitesArray)
print(testArray)


# index methode

print(testArray.index('Spass')) # => 3


# range anschauen
print(testArray[2:4])

# funktion fuer jedes element einzeln printen definieren
def arrayEinzelnAusgeben(arrayName):

#syntax in naiv
#    for element in range(len(arrayName)):

#syntax in python und smart
    for element in arrayName:
        print(element)

arrayEinzelnAusgeben(testArray)


# weitere array methoden die man mal gehoert haben darf: insert, pop, reverse, remove, clear