import random
import config

def getNumberofDice(rollString):
	return int(rollString[0:rollString.find("d")])

def getNumberOfSides(rollString):
	return int(rollString[-(len(rollString) - 1 - len(str(numberOfDice))):])

def findStartOfRoll(commandLocation):
	return commandLocation + config.LENGTH_OF_INITIALIZER_COMMAND

def findEndOfRoll(commentBody, startOfRoll):
	startOfRollToEndOfComment = commentBody[startOfRoll:]
	endOfCommandInSubString = startOfRollToEndOfComment.find(" ")
	endOfCommandInOriginalComment = startOfRoll + endOfCommandInSubString
	return endOfCommandInOriginalComment


def parseDiceInfo(commentBody):
	locationOfCommandInComment = commentBody.find(config.ROLL_INITIALIZER_COMMAND)
	beginningofRollinCommand = findStartOfRoll(locationOfCommandInComment)
	endOfRollInCommand = findEndOfRoll(commentBody, beginningofRollinCommand)
	if endOfRollInCommand - beginningofRollinCommand is -1:
		rollString = commentBody[beginningofRollinCommand:]
	else:
		rollString = commentBody[beginningofRollinCommand:endOfRollInCommand]
	numberofDice = getNumberOfDice(rollString)
	numberOfSides = getNumberOfSides(rollString)
	return [numberOfDice, numberOfSides]


def rollDice(numberOfDice, numberOfSides):
	valueOfDiceRoll = 0
	for die in range(1, numberOfDice):
		currentRoll = config.MINIMUM_DICE_ROLL + int(round(random.random() * numberOfSides))
		valueOfDiceRoll += currentRoll
	return valueOfDiceRoll