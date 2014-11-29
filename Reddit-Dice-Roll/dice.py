import random
import config

def getNumberOfDice(rollString):
	beginningOfDiceNum = 0
	seperatorBetweenDiceAndSides = "d"
	endOfDiceNum = rollString.find(seperatorBetweenDiceAndSides)
	numberOfDice = rollString[beginningOfDiceNum:endOfDiceNum]
	return int(numberOfDice)

def getNumberOfSides(rollString):
	return int(rollString[rollString.find("d")+1:])

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
	numberOfDice = getNumberOfDice(rollString)
	numberOfSides = getNumberOfSides(rollString)
	return [numberOfDice, numberOfSides]


def rollDice(numberOfDice, numberOfSides):
	print numberOfDice
	print numberOfSides
	valueOfDiceRoll = 0
	for die in range(0, numberOfDice):
		currentRoll = config.MINIMUM_DICE_ROLL + int(round(random.random() * numberOfSides))
		print "currentRoll ", currentRoll
		valueOfDiceRoll += currentRoll
	return valueOfDiceRoll