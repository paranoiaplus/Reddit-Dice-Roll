#!/usr/bin/env

import praw
import random
from config import *

#Config Variables


############

#Setup Variables
r = praw.Reddit(user_agent=USER_AGENT)
r.login(USERNAME, PASSWORD)
completedRolls = set()

#############

def determineRollInfo(commentBody):
    commandLocation = commentBody.find("!Roll ")
    startOfRoll = commandLocation + 6 #Location where roll starts
    endOfRoll = commentBody[startOfRoll:].find(" ") + startOfRoll #Location where roll ends
    if endOfRoll - startOfRoll is -1:
        rollString = commentBody[startOfRoll:]
    else:
        rollString = commentBody[startOfRoll:endOfRoll]
    numberOfDice = int(rollString[0:rollString.find("d")])
    numberOfSides = int(rollString[-(len(rollString) - 1 - len(str(numberOfDice))):]) #OH GOD WHY
    infoArray = [numberOfDice, numberOfSides]
    print("Determined Roll Info!")
    return infoArray

def resultingRoll(infoArray):
    rollToReturn = 0
    for i in range (0, infoArray[0]):
        newRoll = 1 + round((random.random() * infoArray[1]))
        rollToReturn += newRoll
        print "Roll " + str(i + 1) + " out of " + str(infoArray[0]) + " = " + str(newRoll)
    return rollToReturn



def scanComments():
    all_comments = r.get_comments(SUBREDDIT)
    for comment in all_comments:
        if "!Roll" in comment.body and comment.id not in completedRolls:
            replyString = ''
            print "Found a roll comment!"
            print("Determining Roll Info...")
            infoArray = determineRollInfo(comment.body)
            replyString += "You're rolling " + str(infoArray[0]) + " dice with " + str(infoArray[1]) + " sides each.\n"
            print("Rolling....")
            replyString += "\nYour resulting roll is: **" + str(resultingRoll(infoArray)) + "**!\n"
            replyString += "\n---\nPM /u/paranoiaplus for any suggestions or recommendations. Source code found [here](https://github.com/paranoiaplus/Reddit-Dice-Roll-Bot/)."
            comment.reply(replyString)
            print("Comment made!")
            print("\nSearching...\n")
            completedRolls.add(comment.id)
    



print("Logged in, starting search...")
while True:
    try:
        scanComments()
    except Exception as e:
        print("Error: ", str(e))









