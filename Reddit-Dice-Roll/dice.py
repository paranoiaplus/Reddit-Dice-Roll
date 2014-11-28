import random
import config

# def getNumberOfSides():

# def getNumberofDice():

# def parseDiceInfo():
	## call getNumberOfSides and getNumberofDice
	## return list
	## [0] = numsides
	## [1] == numDice





# Old
# def determineRollInfo(commentBody):
#     """Determines information of a roll i.e. the number of dice and sides per dice.
#     Returns array with indices; the first being the number of dice and the second
#     being number of sides per die."""
#     commandLocation = commentBody.find("!Roll ")
#     startOfRoll = commandLocation + 6       # Location where roll starts
#     endOfRoll = commentBody[startOfRoll:].find(" ") + startOfRoll       # Location where roll ends
#     if endOfRoll - startOfRoll is -1:
#         rollString = commentBody[startOfRoll:]
#     else:
#         rollString = commentBody[startOfRoll:endOfRoll]
#     numberOfDice = int(rollString[0:rollString.find("d")])
#     numberOfSides = int(rollString[-(len(rollString) - 1 - len(str(numberOfDice))):])       # -1 accounts for the "d" in rollString 
#     infoArray = [numberOfDice, numberOfSides]
#     return infoArray





def rollDice(diceRollInformation):
	numberOfSides = diceRollInformation[0]
	numberOFDice = diceRollInformation[1]
	valueOfDiceRoll = 0
	for die in range(1, numberOfDice):
		currentRoll = config.MINIMUM_DICE_ROLL + int(round(random.random() * numberOfSides))
		valueOfDiceRoll += currentRoll
	return valueOfDiceRoll