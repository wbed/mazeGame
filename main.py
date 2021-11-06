"""
CONT TUNNEL 1
"""

import random
import time
import tavern
import useful

def convertInventoryTxt():
    playerInventory = []
    f5 = open("inventory.txt", "r")
    for line in f5:
        details3 = line.split(",")
        playerInventory.append(details3)
    return playerInventory

def convertInventoryInt(playerInventory):
    for i in range(1, len(playerInventory)):
        playerInventory[i][1] = int(playerInventory[i][1])
    return playerInventory


def convertInventory():
    playerInventory = convertInventoryTxt()
    playerInventory = convertInventoryInt(playerInventory)
    return playerInventory




def enemySearch(enemyList, enemyName, number):
    for i in range(0, len(enemyList)):
        if enemyList[i][0] == enemyName:
            secondValue = enemyList[i][number]
    return secondValue





def introduction():
    print("\n=====")
    print("DAY 1")
    print("=====\n")
    playerName = "PLACEHOLDER"
    print(
        '"Groggy, you slowly wake up, opening your eyes and gazing up at the huge pit that you fell down. \nRubbing your sore head and mumbling curses, you wrench yourself up off the ground, and gaze around the \ncavernous space. You stand up, and walk off of the elevated platfrom you fell onto, and with a monumental \ngroan, the pit somehow closes. This space is now illuminated with torchlight. Your gaze shifts onto a \ndifferent, smaller pedestal. Slowly, you walk up to this mysterious pedestal, before you spot a small velvet \npouch. Taking this pouch, you move on through the chamber. Walking through a tunnel, you arrive at an even \nlarger chamber- with vines littering the walls, huge cracks in the pillars holding the whole space up- \nseemingly ancient altars stand in the 4 corners of the room. In the centre, you spot a diminutive man \npacking up his wares.')
    input("> ")
    print('He spots you, shouting, "Oi, you! What is your name?"')
    input("> ")
    print(
        "Confused, you stand there in silence, struggling to recollect your name. Relieved, you remember your \nname, telling him-")
    flag10 = True
    while flag10 == True:
        playerName = input("Your name is: ")
        ifName = input(f"Is your name definitely {playerName}?(y/n): ")
        if ifName == "y":
            flag10 = False
            input("> ")
        elif ifName == "n":
            flag10 = True
        else:
            print("Invalid Input.")

    print(f'Hi {playerName}! He says. "Do you want to buy anything from my shop? How much gold have you got on you?"')
    input("> ")
    print("You tell him that you have no idea what he's talking about...")
    input("> ")
    print1 = "You didn't fall from up there did you? You're the first one we've had in years!"
    print2 = "Well, I'd better give you the run down. The main thing- there is no way to escape. Believe me, I've tried, \nmy parents tried, everybody has tried at one point or another- there's simply no way to get out."
    print('"' + print1 + '", he exclaims with a gleeful \ngrin. "' + print2 + '"')
    input("> ")
    print(
        "Struck by the gravity of your situation, you tell him that you are going to find a way out, one way or another!")
    input("> ")
    print(
        "Then, you ask him where you can go to stay the night. He tells you that part of the way through the first tunnel, \nyou can find his brother's tavern. He promises that his brother is very hospitable, and you'll be able to stay the night there.")
    input("> ")
    print(
        "You thank the man for his help, and walk down into the first tunnel- noticing a faint red hue coming from it.")
    input("> ")
    print("Before you walk in, you check the inside of the velvet pouch you picked up earlier, and find a 4 sided die!")
    input("> ")
    print('You place the die back inside its pouch, and the man hastily shouts at you- "Hey, did you know you can open your inventory with the E Key?".')
    playerInventory[20][1] = 1  # location = 1
    useful.printInventory(playerInventory, playerName, True)  # canQuit == True
    return playerName, playerInventory


def tunnel1P1(playerName, playerInventory):
    print("\n=============================================")
    print("------------------TUNNEL 1-------------------")
    print("=============================================")
    playerInventory, dead = enemyEnc1(playerInventory)  # first 2 enemies
    return playerInventory, dead


def tunnel1P2(playerName, playerInventory, dead):
    playerInventory[20][1] = 3  # location = 3
    playerInventory = tavern.tavern(playerName, playerInventory, True, dead)  # first tavern
    flag = True
    i = 0
    while flag == True:
        if i > 0:
            playerInventory = tavern.tavern(playerName, playerInventory, False, dead)
        playerInventory = enemyEnc2(playerInventory)  # enemyEnc2
        if playerInventory[21][1] == 1:
            i = i + 1
        else:
            flag = False
    return playerInventory


def tunnel1P3(playerName, playerInventory, dead):
    print("PLCHLDR")


def enemyEnc1(playerInventory):
    for i in range(0, 1):
        print3 = "Hey! What you got there? That pouch will look real great in my pocket!"
        print(f'Soon after you arrive in the tunnel, a thug appears, yelling-\n"{print3}"')
        useful.printInventory(playerInventory, playerName, False)  # canQuit == False
        print(
            "You refuse to hand over your only possession, so the thug says that he'll prise the pouch from your dead body.")
        playerInventory, dead = fightSingleEnemy("Thug", enemyList, playerInventory)
        if dead == True:
            playerInventory[20][1] = 2
            break
        print("Before you leave, you see something the thug dropped- a GOLD POUCH!")
        print("You place your recently earned coin inside the pouch.")
        print("You carry on walking down the tunnel, and a second thug approaches.")
        print5 = "You killed my brother!"
        print6 = "You'll die for that!"
        print(f'"{print5}", he screamed. "{print6}"')
        useful.printInventory(playerInventory, playerName, False)
        playerInventory, dead = fightSingleEnemy("Thug", enemyList, playerInventory)
        if dead == True:
            playerInventory[20][1] = 2
            break
        print("After pushing your way past the second thug, you sigh in relief.")
        playerInventory[20][1] = 2
        useful.printInventory(playerInventory, playerName, True)
    return playerInventory, dead


def enemyEnc2(playerInventory):
    for i in range(0, 1):
        print(
            "The appearance of the tunnel suddenly changes, from the mystical, overgrown appearance of the centre room to a more rustic, town-like atmosphere.\nYou walk down various cobbled streets, hearing the echoes of your feet against the stone.\nSuddenly, an armoured thug appears!")
        useful.printInventory(playerInventory, playerName, False)
        playerInventory, dead = fightSingleEnemy("Armoured Thug", enemyList, playerInventory)
        if dead == True:
            playerInventory[21][1] = 1
            break
        print("Wary of more enemies, you carry on worming your way around the identical-looking streets.")
        print("After wandering for a while, you encounter a SILVER CHEST!")
        print("In the silver chest, you find a LUCKY POTION!")
        playerInventory[7][1] = 1
        print("After you drink the potion, a street gang appears, saying that the chest was their property!")
        print('The lead thug shouts- "Ur gonna pay for this!"')
        print("The first thug rushes forward...")
        playerInventory, dead = fightSingleEnemy("Thug", enemyList, playerInventory)
        if dead == True:
            playerInventory[21][1] = 1
            break
        print("Another thug attacks you!")
        playerInventory, dead = fightSingleEnemy("Thug", enemyList, playerInventory)
        if dead == True:
            playerInventory[21][1] = 1
            break
        print("A more heavily armoured thug appears out of nowhere to defend his leader.")
        playerInventory, dead = fightSingleEnemy("Armoured Thug", enemyList, playerInventory)
        if dead == True:
            playerInventory[21][1] = 1
            break
        print("Shocked that you dealt with all of his henchmen, the lead thug fights you himself!")
        playerInventory, dead = fightSingleEnemy("Lead Thug", enemyList, playerInventory)
        if dead == True:
            playerInventory[21][1] = 1
            break
        print(
            "Exasperated by the fact that you managed to defeat an entire gang of thugs, you carry on walking down the endless cobbled streets.")
        playerInventory[20][1] = 3
        useful.printInventory(playerInventory, playerName, True)
    return playerInventory


def fightSingleEnemy(enemyName, enemyList, playerInventory):
    enemyArmour, enemyLives, enemyDiceHigher, enemyDice2, enemyDice2Higher, enemyGold = enemyTranslate(enemyName,
                                                                                                       enemyList)
    print(f"\n{enemyName} challenged you!")
    dieHigher, die2Have, die2Higher, playerArmour, goldBalance, treasure, luckypotion, smokebottle, attackpotion, playerLives, tunnel1Clear, tunnel2Clear, tunnel3Clear, tunnel4Clear, enemiesKilled, goblinGamesWon, goblinGamesLost, tunnelsCleared, location = useful.convertFromInventory(
        playerInventory)
    while enemyLives > 0 and playerLives > 0:
        print("=========================")
        print(f"{enemyName}'s lives: {enemyLives}")
        print(f"{playerName}'s lives: {playerLives}")
        print("=========================")
        print("Rolling die...")
        enemyThrow = random.randint(1, enemyDiceHigher)
        playerThrow = playerDiceThrow(playerInventory)
        enemyScore = enemyThrow - playerInventory[5][1]
        print(
            f"{enemyName} rolled a {enemyThrow}. (Opponent's throw: {enemyThrow} - Your Armour: {playerArmour} = Score: {enemyScore})")
        if playerInventory[7][1] == 1:
            playerLuck = random.randint(1, 20)
            if playerLuck == 5:
                print("Your lucky potion negates the damage your opponent dealt!")
                print(f"{enemyName}'s Score: 0")
                enemyScore = 0
        playerScore = playerThrow - enemyArmour
        print(
            f"You rolled a {playerThrow}. (Your throw: {playerThrow} - Opponent's Armour: {enemyArmour} = Score: {playerScore})")
        useful.printInventory(playerInventory, playerName, False)
        if playerScore > enemyScore:
            print("After a brief scuffle, you manage to land a hit on your opponent.")
            enemyLives = enemyLives - 1
        elif enemyScore > playerScore:
            print("After a few sloppy attacks, you are easily bested by your opponent.")
            playerLives = playerLives - 1
        elif enemyScore == playerScore:
            print("Neither you, or your opponent manage to find the upper hand.\n")
    if enemyLives == 0:
        goldBalance = goldBalance + enemyGold
        dead = False
        print("You step over your opponent's body, and move on.")
        print(f"You found {enemyGold} Gold!")
        print(f"Your total gold balance is now {goldBalance}.")
        enemiesKilled = enemiesKilled + 1
    elif playerLives == 0:
        print("Your opponent manages to break your defence, and attacks you.")
        print("You black out.")
        dead = True
    playerInventory[11][1] = playerLives
    playerInventory[10][1] = goldBalance
    playerInventory[16][1] = enemiesKilled
    useful.printInventory(playerInventory, playerName, False)
    return playerInventory, dead


def playerDiceThrow(playerInventory):
    playerThrow = random.randint(1, playerInventory[2][1])
    if playerInventory[3][1] != 0:
        playerThrow2 = random.randint(1, playerInventory[4][1])
        if playerThrow > playerThrow2:
            playerThrow = playerThrow
        elif playerThrow2 > playerThrow:
            playerThrow = playerThrow2
        else:
            playerThrow = playerThrow

    playerThrow = playerInventory[9][1] + playerThrow
    return playerThrow


def enemyTranslate(enemyName, enemyList):
    enemyArmour = enemySearch(enemyList, enemyName, 1)
    enemyLives = enemySearch(enemyList, enemyName, 2)
    enemyDiceHigher = enemySearch(enemyList, enemyName, 3)
    enemyDice2 = enemySearch(enemyList, enemyName, 4)
    enemyDice2Higher = enemySearch(enemyList, enemyName, 5)
    enemyGold = enemySearch(enemyList, enemyName, 6)
    return enemyArmour, enemyLives, enemyDiceHigher, enemyDice2, enemyDice2Higher, enemyGold


def playerNameConv(playerInventory):
    playerName = useful.playerInventorySearch(playerInventory, "name")
    return playerName


def gameMenu():
    print("====================================")
    print("-------------MAZE-GAME--------------")
    print("====================================")
    flag = True
    while flag == True:
        gameIf = input("\nStart Game? [1]"
                       "\nContinue Game? [2]"
                       "\nView your Statistics. [3]"
                       "\nExit Game. [4]: ")
        if gameIf == "1":
            gameIf2 = "start"
            ifIf = input("\nWARNING- THIS WILL OVERWRITE YOUR PROGRESS AND START A NEW GAME:"
                         "\nDo you still wish to proceed?(y/n): ")
            if ifIf == "y":
                flag = False
            elif ifIf == "n":
                print("Returning to menu...")
                flag = True
            else:
                print("Invalid Input.")
        elif gameIf == "2":
            gameIf2 = "continue"
            flag = False
        elif gameIf == "3":
            gameIf2 = "stats"
            print("Opening statistics page...")
            print()
            printStats(playerInventory)
        elif gameIf == "4":
            print("Exiting game...")
            time.sleep(1)
            quit()
        else:
            print("Invalid Input.")
    return gameIf2


# INVENTORY
# playerInventory = [["name", "PLACEHOLDER"], ["die1", 1], ["dieHigher", 4], ["die2", 0], ["die2Higher", 0], ["armour", 1], ["treasure", 0], ["luckypotion", 0], ["smokebottle", 0], ["attackpotion", 0], ["goldBalance", 0], ["lives", 5], ["tunnel1Clear", 0], ["tunnel2Clear", 0], ["tunnel3Clear", 0], ["tunnel4Clear", 0], ["enemiesKilled", 0], ["goblinGamesWon", 0], ["goblinGamesLost", 0], ["tunnelsCleared", 0], ["location", 0]]

def resetGame(playerInventory):
    playerInventory = [["name", "PLACEHOLDER"], ["die1", 1], ["dieHigher", 4], ["die2", 0], ["die2Higher", 0],
                       ["armour", 1], ["treasure", 0], ["luckypotion", 0], ["smokebottle", 0], ["attackpotion", 0],
                       ["goldBalance", 0], ["lives", 5], ["tunnel1Clear", 0], ["tunnel2Clear", 0], ["tunnel3Clear", 0],
                       ["tunnel4Clear", 0], ["enemiesKilled", 0], ["goblinGamesWon", 0], ["goblinGamesLost", 0],
                       ["tunnelsCleared", 0], ["location", 0], ["dead", 0]]
    return playerInventory


def printStats(playerInventory):
    goldBalance = playerInventory[10][1]
    enemiesKilled = playerInventory[16][1]
    goblinGamesWon = playerInventory[17][1]
    goblinGamesLost = playerInventory[18][1]
    tunnelsCleared = playerInventory[19][1]
    print("========================")
    print(f"Enemies Killed: {enemiesKilled}")
    print(f"Goblin Games Won: {goblinGamesWon}")
    print(f"Goblin Games Lost: {goblinGamesLost}")
    print(f"Tunnels Cleared: {tunnelsCleared}")
    print(f"Gold Balance: {goldBalance}")
    print("========================")



# ENEMIES = [enemyName, enemyArmour, enemyLives, enemyDiceHigher, enemyDice2, enemyDice2Higher, enemyGold]
enemyList = [["Thug", 0, 1, 3, 0, 0, 5], ["Armoured Thug", 1, 1, 4, 0, 0, 10], ["Lead Thug", 1, 2, 5, 1, 3, 15]]

# hint array
"""
[
  ["Don't go near the fire-breathing dragons..."], ["Swords are sharp and pointy."], ["You probably shouldn't drink poison.."], ["If a man comes up to you claiming to be a saint, he's probably lying!"], ["Never, ever trust a dwarf."], ["With great power comes great responsibility."], ["Substance abuse is no joke!- don't drink too many potions!"], ["I know a guy in a far away village who loves treasure!"], ["Definitely run away from a troll."], ["Don't try to escape. You'll die trying."]
]
"""

# rules
"""
If you run out of lives, you wake up in the last tavern with between 30-70% of your gold gone, and with 50% of your treasure, and no potions + bottles.
"""
playerInventory = convertInventory()
gameIf2 = gameMenu()
if gameIf2 == "start":
    print("Starting new game...")
    playerInventory = resetGame(playerInventory)
elif gameIf2 == "continue":
    print("Continuing game...\n")  # find area num + go to
playerName = playerNameConv(playerInventory)

# FINDING LOCATION

dead = playerInventory[21][1]
location = playerInventory[20][1]

if dead == 0:
    dead = False

if location == 0:
    playerName, playerInventory = introduction()
    location = playerInventory[20][1]

if location == 1:
    playerInventory, dead = tunnel1P1(playerName, playerInventory)
    location = playerInventory[20][1]

if location == 2:
    playerInventory = tunnel1P2(playerName, playerInventory, dead)
    location = playerInventory[20][1]

if location == 3:
    tunnel1P3(playerName, playerInventory, dead)

"""
playerName = introduction()
playerInventory = tunnel1P1(playerName, playerInventory)
"""
# tavern(playerName, playerInventory, False, dead) # ORDINARY TAVERN
useful.saveProgress(playerInventory, playerName) # saves progress
# INPUT THING: printInventory(playerInventory, playerName)