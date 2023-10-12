import random

def generateArray(rangeSize):
    returnArray = []
    for count in range(rangeSize):
        returnArray.append(count + 1)
    return returnArray

def drawFromArray(arrayToAppend, arrayToDrawFrom):
    arrayToAppend.append(arrayToDrawFrom.pop(random.randint(0, len(arrayToDrawFrom) - 1)))
    return arrayToAppend

def drawNumbers(numberCount, rangeSize):
    numbersToReturn = []
    poolToDraw = generateArray(rangeSize)
    for numberDrawn in range(numberCount):
        drawFromArray(numbersToReturn, poolToDraw)
    return numbersToReturn

lotteryNumbers = drawNumbers(6, 49)
print(lotteryNumbers)