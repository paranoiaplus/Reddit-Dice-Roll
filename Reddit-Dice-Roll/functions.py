import dice
import config
import praw


# Login
redditClient = praw.Reddit(user_agent=config.USER_AGENT)
redditClient.login(config.USERNAME, config.PASSWORD)


###########
completedRolls = set()
###########
def commentIsNew(commentID):
    if commentID not in completedRolls:
        return True
    else:
        return False

def hasRollCommand(commentBody):
    if config.COMMAND_INITIALIZER in commentBody:
        return True
    else:
        return False

def constructReplyString(diceInfo):
    numberOfSides = diceRollInfo[0]
    numberOFDice = diceRollInfo[1]
    rollResult = dice.rollDice(diceInfo)
    replyString = "You're rolling " + str(infoArray[0]) + " dice with " + str(infoArray[1]) + " sides each.\n"
    replyString += "\nYour resulting roll is: **" + str(resultingRoll(infoArray)) + "**!\n"
    replyString += "\n---\nPM /u/paranoiaplus for any suggestions or recommendations. Source code found [here](https://github.com/paranoiaplus/Reddit-Dice-Roll-Bot/)."
    return replyString

def scanComments():
    recentComments = r.get_comments(config.SUBREDDIT)
    for comment in recentComments:
        if hasRollCommand(comment.body) and commentIsNew(comment.id):
            diceRollInfo = dice.parseDiceInfo(comment.body)
            commentReplyString = constructReplyString(diceRollInfo)
            comment.reply(commentReplyString)
            completedRolls.append(comment.id)








