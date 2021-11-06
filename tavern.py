import cardGame
import diceGame
import random
import useful

def details(playerName):
    player1Name = playerName
    player2Name = "the goblin"
    return player1Name, player2Name

def goblin(goldIn, playerName):
    player1Name, player2Name = details(playerName)
    flag4 = True
    while flag4 == True:
        print("The goblin asks you what game you want to play.")
        gameIf = input("\n[D]ice game or [C]ard game?: ")
        if gameIf.upper() == "D":
            print("Now Playing: Dice Game.")
            flag4 = False
            doAgain, goldIn, player2Wins = diceGame.diceGame(player1Name, player2Name, goldIn)
            if doAgain == "y":
                flag4 = True
            elif doAgain == "n":
                flag4 = False
                goblinFin = True
        elif gameIf.upper() == "C":
            print("Now Playing: Card Game.")
            flag4 = False
            doAgain, goldIn, player2Wins = cardGame.cardGame(player1Name, player2Name, goldIn)
            if doAgain == "y":
                flag4 = True
            elif doAgain == "n":
                flag4 = False
                goblinFin = True
        else:
            print("Invalid Input.\n")
    return goblinFin, goldIn, player2Wins

def tavern(playerName, playerInventory, firstVisit, dead):
    dead = playerInventory[21][1]
    hintSheet = [["Don't go near the fire-breathing dragons..."], ["Swords are sharp and pointy."],
                 ["You probably shouldn't drink poison.."],
                 ["If a man comes up to you claiming to be a saint, he's probably lying!"],
                 ["Never, ever trust an orc."], ["With great power comes great responsibility."],
                 ["Substance abuse is harmful- don't drink too many potions!"],
                 ["I know my brother really loves treasure!"], ["Definitely run away from a troll."],
                 ["Don't try to escape. You'll die trying."]]
    goblinFin = False
    dieHigher, die2Have, die2Higher, armour, goldBalance, treasure, luckypotion, smokebottle, attackpotion, lives, tunnel1Clear, tunnel2Clear, tunnel3Clear, tunnel4Clear, enemiesKilled, goblinGamesWon, goblinGamesLost, tunnelsCleared, location = useful.convertFromInventory(
        playerInventory)
    flag9 = True
    if dead == True:
        playerInventory = useful.playerDied(playerInventory)
        dieHigher, die2Have, die2Higher, armour, goldBalance, treasure, luckypotion, smokebottle, attackpotion, lives, tunnel1Clear, tunnel2Clear, tunnel3Clear, tunnel4Clear, enemiesKilled, goblinGamesWon, goblinGamesLost, tunnelsCleared, location = useful.convertFromInventory(
            playerInventory)
        print("You wake up, sprawled across a couch in the tavern.")
        print(
            "The friendly adventurer next to you explains that he found you knocked out on his travels,\nand brought you to the nearest tavern.")
        print("You regain your composure, and check your adventurer's satchel.")
        lives = 3
        useful.printInventory(playerInventory, playerName, False)
        print(
            f"You have: {goldBalance} Gold; {treasure} Treasure; {lives} Lives; and all your potions have disappeared and their affects worn off.")
    else:
        print("You open the next door, and step into the cozy, relative safety of the tavern.")
    visitedWeaponsmith = False
    if firstVisit == True:
        print("The man's brother approaches you, asking what you want for a drink-")
        print("You tell him that you want a place to stay.")
        useful.printInventory(playerInventory, playerName, False)
        print('"Well... That will cost you. 20 Gold."')
        useful.printInventory(playerInventory, playerName, False)
        print('"Wait!", you say- you cannot afford that!')
        print("You explain that you are a friend of his brother's, and he lets you stay for free.")
        useful.printInventory(playerInventory, playerName, False)
        print("=====")
        print("DAY 2")
        print("=====")
        print("The next day, you wake up and walk downstairs.")
        useful.printInventory(playerInventory, playerName, False)
    else:
        useful.printInventory(playerInventory, playerName, False)
    print(f'The inkeep approaches you, bellowing, "Hey!- {playerName}, welcome back!"')
    if lives == 1:
        lives = lives + 1
        print("He gives you some hearty food as payment for clearing out the foes on the path.")
        print(f"Your life total increased by 1 to {lives}!")
    print('"What do you want to do?"')
    flag2 = True
    while flag2 == True:
        print("")
        whatDo = input("Gamble with the Goblin?[1]"
                       "\nVisit the weaponsmith?[2]"
                       "\nFind out about what this place is about?[3]"
                       "\nNothing.[4]: ")
        print()
        if whatDo == "1":
            if goblinFin == True:
                print("Nice try, you've already gambled enough!")
            elif goblinFin == False:
                print("As you walk over to the goblin's table, you check your gold balance.")
                for i in range(0, 1):
                    if goldBalance == 0:
                        print("You have no money at all, so unfortunately you can't bet anything.")
                        break
                    print(f"At the moment, you have {goldBalance} gold.")
                    while flag9 == True:
                        goldIn = input("How much gold do you want to play with?: ")
                        goldIn = int(goldIn)
                        if goldIn > goldBalance:
                            print("The goblin complains that you don't actually have that much money...")
                            print("You can't gamble on thin air, you know!")
                        elif goldIn == 0:
                            print("The goblin laughs at you.")
                            print("Did you understand me?, he asks. You can't gamble with no money at all!")
                        elif goldIn < goldBalance:
                            print("You take the gold out of your pouch, place it on the table and take a seat.")
                            flag9 = False
                        elif goldIn == goldBalance:
                            print("Woah, that's all of your money- feeling bold today I see...")
                            print("The goblin says, rubbing his hands with glee.")
                            flag9 = False
                    goldBalance = goldBalance - goldIn
                    goblinFin, goldIn, player2Wins = goblin(goldIn, playerName)
                    if player2Wins != True:
                        goldBalance = goldBalance + goldIn
                        goblinGamesWon = goblinGamesWon + 1
                    else:
                        goblinGamesLost = goblinGamesLost + 1
                        goldBalance = goldBalance
                    print(f"Your new gold balance: {goldBalance} Gold.")
        elif whatDo == "2":
            if visitedWeaponsmith == False:
                visitedWeaponsmith = True
                if dieHigher == 4:
                    print(
                        f"Hey, {playerName}! You've done such a great job clearing out those pesky thugs, i'll give you a little something!")
                    print("You recieved the 6 sided die!")
                    dieHigher = 6
                else:
                    die = random.randint(1,2)
                    if die == "2":
                        print("She says that she's got something for you!")
                        if (die2Have == 1) and (die2Higher == 4) and (tunnel2Clear == 1):
                            print("For 100G, do you want to upgrade your second die?(y/n): ")  # 4-6 on second die
                        elif die2Have == 0:
                            print("For 200G, do you want to fully upgrade your first die?(y/n): ")  # 6-8 on first die
                        elif (die2Have == 1) and (die2Higher == 6) and (tunnel3Clear == 1):
                            print("For 500G, do you want to fully upgrade your second die?(y/n): ")  # 6-8 on second die
                    else:
                        print("Unfortunately, the weaponsmith doesn't have any stock for you today.")
            else:
                print("Sorry, you already talked to her!")

        elif whatDo == "3":
            print("You're in the maze right now- and before you think about escaping, most of us were born here.")
            print("Our parents, our parents' parents, and their parents too all lived and died in this forsaken place.")
            print("Tales of the outside world are few and far between, and people like you-")
            print("Who haven't lived their whole lives under torchlight are considered an oddity.")
            print("You may have an idea about how to escape, but all of us have simply given up hope.")
            print("Good luck though!")
        elif whatDo == "4":
            print(f"{playerName}, wait!")
            print("Try and win something before you go!\n")
            print("Rolling die...")
            die = random.randint(1, dieHigher)
            print(f"You rolled a {die}.")
            if die == 1:
                print("You won a pouch of gold (+2 Gold).")
                goldBalance = goldBalance + 2
            elif die == 2:
                print("You won a +1 attack potion!")
                attackpotion = 1
            elif die == 3:
                die3 = random.randint(1, 15)
                if die3 == 15:
                    print("You were pretty lucky!")
                    print("You won an armour blessing!")  # permanent + 1 armour increase
                    armour = armour + 1
                else:
                    print(
                        "You won some treasure! The inkeep says that his brother really loves that stuff...")  # can sell to brother in main room for 20G
                    treasure = treasure + 1
            elif die == 4:
                print("You didn't win anything...")
            elif die == 5:
                print("You won a hint!")
                hintNum = random.randint(1, 10)
                hint = hintSheet[hintNum]
                print(f"{hint}")  # hint
            elif die == 6:
                print("You won a lucky potion!")  # 5% chance to not take a hit of damage until next tavern
                luckypotion = 1
            elif die == 7:
                print("You won a smoke bottle!")  # escape from an encounter
                smokebottle = 1
            elif die == 8:
                print("You won a life potion!")  # 1 extra life
                lives = lives + 1
            flag2 = False
            print("\nSatisfied you got what you needed, you walk out of the tavern, and continue on your journey.")
            playerInventory = useful.convertToInventory(playerInventory, dieHigher, die2Have, armour, treasure, luckypotion,
                                                 smokebottle, attackpotion, goldBalance, lives, tunnel1Clear,
                                                 tunnel2Clear, tunnel3Clear, tunnel4Clear, enemiesKilled,
                                                 goblinGamesWon, goblinGamesLost, tunnelsCleared, location)
    return playerInventory