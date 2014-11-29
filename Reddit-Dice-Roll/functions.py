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
    if config.ROLL_INITIALIZER_COMMAND in commentBody:
        return True
    else:
        return False

def constructReplyString(diceInfo):
    numberOfDice = diceInfo[0]
    numberOfSides = diceInfo[1]
    rollResult = dice.rollDice(numberOfDice, numberOfSides)
    replyString = "You're rolling " + str(numberOfDice) + " dice with " + str(numberOfSides) + " sides each.\n"
    replyString += "\nYour resulting roll is: **" + str(rollResult) + "**!\n"
    replyString += "\n---\nPM /u/paranoiaplus for any suggestions or recommendations. Source code found [here](https://github.com/paranoiaplus/Reddit-Dice-Roll-Bot/)."
    return replyString

def scanComments():
    recentComments = redditClient.get_comments(config.SUBREDDIT)
    for comment in recentComments:
        if hasRollCommand(comment.body) and commentIsNew(comment.id):
            diceRollInfo = dice.parseDiceInfo(comment.body)
            commentReplyString = constructReplyString(diceRollInfo)
            comment.reply(commentReplyString)
            completedRolls.add(comment.id)