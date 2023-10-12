#long, hopefully easier to understand and maintain
 
import random

def generateArray(rangeSize: int):
    '''returns an Array with integer elements from 1 to rangeSize'''
    returnArray = list(range(1, rangeSize + 1))
    return returnArray

def drawFromArray(arrayToAppend: str, arrayToDrawFrom: str):
    '''removes elements from arrayToDrawFrom and appends them to arrayToAppend'''
    arrayToAppend.append(arrayToDrawFrom.pop(random.randint(0, len(arrayToDrawFrom) - 1)))
    return arrayToAppend

def drawNumbers(numberCount: int, rangeSize: int):
    '''draws numberCount elements from a pool of numbers in a range from 1 to rangeSize without duplicates and puts them in an array.
    
    returns the generated array.'''
    numbersToReturn = []
    poolToDraw = generateArray(rangeSize)
    for numberDrawn in range(numberCount):
        drawFromArray(numbersToReturn, poolToDraw)
    return numbersToReturn

lotteryNumbers = drawNumbers(6, 49)
print(lotteryNumbers)


#short, possibly harder to maintain and read


import random

def drawNumbers(numberCount: int, rangeSize: int):
    '''returns an array containing numberCount integer elements in a range from 1 to rangeSize without duplicates.'''
    poolToDraw = list(range(1, rangeSize + 1))
    return [poolToDraw.pop(random.randint(0, len(poolToDraw) - 1)) for _ in range(numberCount)]

lotteryNumbers = drawNumbers(6, 49)
print(lotteryNumbers)