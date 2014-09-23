""""Functions required for connecting to Reddit, scanning and replying to
comments, and calculating dice rolls."""

import praw
import random
from config import *

r = praw.Reddit(user_agent=USER_AGENT)
r.login(USERNAME, PASSWORD)
completedRolls = set()


def determineRollInfo(commentBody):
    """Determines information of a roll i.e. the number of dice and sides per dice.
    Returns array with indices; the first being the number of dice and the second
    being number of sides per die."""
    commandLocation = commentBody.find("!Roll ")
    startOfRoll = commandLocation + 6       # Location where roll starts
    endOfRoll = commentBody[startOfRoll:].find(" ") + startOfRoll       # Location where roll ends
    if endOfRoll - startOfRoll is -1:
        rollString = commentBody[startOfRoll:]
    else:
        rollString = commentBody[startOfRoll:endOfRoll]
    numberOfDice = int(rollString[0:rollString.find("d")])
    numberOfSides = int(rollString[-(len(rollString) - 1 - len(str(numberOfDice))):])       # -1 accounts for the "d" in rollString 
    infoArray = [numberOfDice, numberOfSides]
    return infoArray

def resultingRoll(infoArray):
    """Calculates each roll for a single request (ex: rolls twice if 2d6). Adds 
    each roll to rollTotal."""
    rollTotal = 0
    for i in range (0, infoArray[0]):
        newRoll = 1 + int(round((random.random() * infoArray[1])))
        rollTotal += newRoll
    return rollTotal

def scanComments():
    """Scans Reddit comments for '!Roll' command, calls other functions, and
    replies to the comments with their roll result."""
    all_comments = r.get_comments(SUBREDDIT)
    for comment in all_comments:
        if "!Roll" in comment.body and comment.id not in completedRolls:
            replyString = ''
            print("Found a roll comment!")
            infoArray = determineRollInfo(comment.body)
            replyString += "You're rolling " + str(infoArray[0]) + " dice with " + str(infoArray[1]) + " sides each.\n"
            replyString += "\nYour resulting roll is: **" + str(resultingRoll(infoArray)) + "**!\n"
            replyString += "\n---\nPM /u/paranoiaplus for any suggestions or recommendations. Source code found [here](https://github.com/paranoiaplus/Reddit-Dice-Roll-Bot/)."
            comment.reply(replyString)
            print("\nReplied to comment!")
            print("\nSearching...\n")
            completedRolls.add(comment.id)