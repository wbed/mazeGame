import random
import time

def playerInventorySearch(playerInventory, firstValue):
    for i in range(0, len(playerInventory)):
        if playerInventory[i][0] == firstValue:
            secondValue = playerInventory[i][1]
    return secondValue


def playerInventoryAdd(playerInventory, firstValue, secondValue):
    for i in range(0, len(playerInventory)):
        if playerInventory[i][0] == firstValue:
            playerInventory[i][1] = secondValue
    return playerInventory

def inventoryToTxt(playerInventory):
    f5 = open("inventory.txt", "r")
    f5.truncate
    f6 = open("inventory.txt", "w")
    for i in range(0, len(playerInventory)):
        for x in range(0, 3):
            if x <= 1:
                filewrite = playerInventory[i][x]
                filewrite = str(filewrite)
                f6.write(filewrite + ",")
            elif x == 2:
                f6.write("\n")

def saveProgress(playerInventory, playerName):
  playerInventory = playerInventoryAdd(playerInventory, "name", playerName)
  inventoryToTxt(playerInventory)

def convertFromInventory(playerInventory):
    dieHigher = playerInventorySearch(playerInventory, "dieHigher")
    die2Have = playerInventorySearch(playerInventory, "die2")
    die2Higher = playerInventorySearch(playerInventory, "die2Higher")
    armour = playerInventorySearch(playerInventory, "armour")
    goldBalance = playerInventorySearch(playerInventory, "goldBalance")
    treasure = playerInventorySearch(playerInventory, "treasure")
    luckypotion = playerInventorySearch(playerInventory, "luckypotion")
    smokebottle = playerInventorySearch(playerInventory, "smokebottle")
    attackpotion = playerInventorySearch(playerInventory, "attackpotion")
    lives = playerInventorySearch(playerInventory, "lives")
    tunnel1Clear = playerInventorySearch(playerInventory, "tunnel1Clear")
    tunnel2Clear = playerInventorySearch(playerInventory, "tunnel2Clear")
    tunnel3Clear = playerInventorySearch(playerInventory, "tunnel3Clear")
    tunnel4Clear = playerInventorySearch(playerInventory, "tunnel4Clear")
    enemiesKilled = playerInventorySearch(playerInventory, "enemiesKilled")
    goblinGamesWon = playerInventorySearch(playerInventory, "goblinGamesWon")
    goblinGamesLost = playerInventorySearch(playerInventory, "goblinGamesLost")
    tunnelsCleared = playerInventorySearch(playerInventory, "tunnelsCleared")
    location = playerInventorySearch(playerInventory, "location")
    return dieHigher, die2Have, die2Higher, armour, goldBalance, treasure, luckypotion, smokebottle, attackpotion, lives, tunnel1Clear, tunnel2Clear, tunnel3Clear, tunnel4Clear, enemiesKilled, goblinGamesWon, goblinGamesLost, tunnelsCleared, location


def convertToInventory(playerInventory, dieHigher, die2Have, armour, treasure, luckypotion, smokebottle, attackpotion,
                       goldBalance, lives, tunnel1Clear, tunnel2Clear, tunnel3Clear, tunnel4Clear, enemiesKilled,
                       goblinGamesWon, goblinGamesLost, tunnelsCleared, location):
    playerInventory = playerInventoryAdd(playerInventory, "dieHigher", dieHigher)
    playerInventory = playerInventoryAdd(playerInventory, "die2", die2Have)
    playerInventory = playerInventoryAdd(playerInventory, "armour", armour)
    playerInventory = playerInventoryAdd(playerInventory, "treasure", treasure)
    playerInventory = playerInventoryAdd(playerInventory, "luckypotion", luckypotion)
    playerInventory = playerInventoryAdd(playerInventory, "smokebottle", smokebottle)
    playerInventory = playerInventoryAdd(playerInventory, "attackpotion", attackpotion)
    playerInventory = playerInventoryAdd(playerInventory, "goldBalance", goldBalance)
    playerInventory = playerInventoryAdd(playerInventory, "lives", lives)
    playerInventory = playerInventoryAdd(playerInventory, "tunnel1Clear", tunnel1Clear)
    playerInventory = playerInventoryAdd(playerInventory, "tunnel2Clear", tunnel2Clear)
    playerInventory = playerInventoryAdd(playerInventory, "tunnel3Clear", tunnel3Clear)
    playerInventory = playerInventoryAdd(playerInventory, "tunnel4Clear", tunnel4Clear)
    playerInventory = playerInventoryAdd(playerInventory, "enemiesKilled", enemiesKilled)
    playerInventory = playerInventoryAdd(playerInventory, "goblinGamesWon", goblinGamesWon)
    playerInventory = playerInventoryAdd(playerInventory, "goblinGamesLost", goblinGamesLost)
    playerInventory = playerInventoryAdd(playerInventory, "tunnelsCleared", tunnelsCleared)
    playerInventory = playerInventoryAdd(playerInventory, "location", location)
    return playerInventory


def playerDied(playerInventory):
    dieHigher, die2Have, die2Higher, armour, goldBalance, treasure, luckypotion, smokebottle, attackpotion, lives, tunnel1Clear, tunnel2Clear, tunnel3Clear, tunnel4Clear, enemiesKilled, goblinGamesWon, goblinGamesLost, tunnelsCleared, location = convertFromInventory(
        playerInventory)
    if goldBalance > 10:
        goldPerc = random.randint(3, 7)
        goldBalance = (goldBalance // 10) * goldPerc
        goldBalance = int(goldBalance)

    if treasure > 1:
        treasure = treasure // 2
        treasure = int(treasure)
    luckypotion = 0
    smokebottle = 0
    attackpotion = 0
    lives = 3
    playerInventory = convertToInventory(playerInventory, dieHigher, die2Have, armour, treasure, luckypotion,
                                         smokebottle, attackpotion, goldBalance, lives, tunnel1Clear, tunnel2Clear,
                                         tunnel3Clear, tunnel4Clear, enemiesKilled, goblinGamesWon, goblinGamesLost,
                                         tunnelsCleared, location)
    return playerInventory


def printInventory(playerInventory, playerName, canQuit):
    if canQuit == True:
        print("\nAutosaving...")
        saveProgress(playerInventory, playerName)

    pause = input("> ")
    if pause.upper() == "E":
        dieHigher, die2Have, die2Higher, armour, goldBalance, treasure, luckypotion, smokebottle, attackpotion, lives, tunnel1Clear, tunnel2Clear, tunnel3Clear, tunnel4Clear, enemiesKilled, goblinGamesWon, goblinGamesLost, tunnelsCleared, location = convertFromInventory(
            playerInventory)
        print("================================================")
        print("You open your satchel. (Using the E Key)")
        print(f"Your first die: {dieHigher}-sided.")
        if die2Have == 1:
            print(f"Your second die: {die2Higher}-sided.")
        print(f"Your armour points: {armour}")
        print(f"Your gold balance: {goldBalance} Gold.")
        print(f"Your treasure balance: {treasure} treasure.")
        print(f"You have {luckypotion} luckypotion/s.")
        print(f"You have {smokebottle} smokebottle/s.")
        print(f"You have {attackpotion} attackpotion/s.")
        print(f"Your lives: {lives}")
        print(f"You have cleared: {tunnelsCleared} tunnel/s.")
        print("================================================")
        doQuit(playerInventory, playerName)


def doQuit(playerInventory, playerName):
    flag10 = True
    while flag10 == True:
        ifQuit = input("Do you want to quit?(y/n): ")
        if ifQuit == "y":
            print("YOU WILL LOSE YOUR PROGRESS UP TO THE LAST AUTOSAVE")
            ifQuit2 = input("Are you sure you want to quit?(y/n): ")
            if ifQuit2 == "y":
              print("Quitting...")
              time.sleep(1)
              quit()
        elif ifQuit == "n":
            print("Returning to main game...\n")
            return
        else:
            print("Invalid Input.")