import random

# DICE GAME
def diceRoll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def diceOut(player1Name, player2Name):
    player1Dice1, player1Dice2 = diceRoll()
    input("\nRoll your dice: ")
    print(f"Your dice: {player1Dice1}, {player1Dice2}")
    player2Dice1, player2Dice2 = diceRoll()
    print("The goblin rolls his dice.")
    print(f"The goblin's dice: {player2Dice1}, {player2Dice2}")
    return player1Dice1, player1Dice2, player2Dice1, player2Dice2


def diceCalc(diceTotal, score, playerName):
    if diceTotal % 2 == 0:
        if playerName == "the goblin":
            print("The goblin's total was even.")
        else:
            print("Your total was even!")
        print("+10 points to score.")
        score = score + 10
    elif diceTotal % 2 != 0:
        if playerName == "the goblin":
            print("The goblin's total was odd...")
        else:
            print("Your total was odd...")
        print("-5 points to score.")
        if score < 5:
            score = 0
        else:
            score = score - 5
    return score


def playerTurn(player1Dice1, player1Dice2, player2Dice1, player2Dice2, player1Score, player2Score, player1Name,
               player2Name):
    input(f"\n{player1Name}'s turn:")
    print(f"{player1Name}'s Dice: {player1Dice1}, {player1Dice2}")
    score = player1Score
    player1Score = calcScore(player1Dice1, player1Dice2, score, player1Name)
    input(f"\nThe goblin's turn:")
    print(f"The goblin's Dice: {player2Dice1}, {player2Dice2}")
    score = player2Score
    player2Name = "The goblin"
    player2Score = calcScore(player2Dice1, player2Dice2, score, player2Name)
    input("Next turn: ")
    return player1Score, player2Score


def calcScore(dice1, dice2, score, playerName):
    diceTotal = dice1 + dice2
    score2 = diceCalc(diceTotal, score, playerName)
    if dice1 == dice2:
        print("You got a double!")
        print("Rolling another die:")
        dice3 = random.randint(1, 6)
        print(f"Your third die: {dice3}")
        score = diceCalc(dice3, score2, playerName)
        print(f"{playerName}'s score: {score}")
    else:
        dice3 = 0

    if dice1 != dice2:
        print(f"{playerName}'s score: {score2}")
        score = score2
    return score

def endGameIf(player1Wins, player2Wins, goldIn):
    if player1Wins == True:
        goldIn = goldIn * 2
        print(f"You won {goldIn} Gold.")
        print("\nThe goblin congratulates you on your winnings, but he proposes a tantalising offer:")
        print(f"You can play again, and double your money- if you want... (You could win {goldIn * 2} Gold).")
        flag6 = True
        while flag6 == True:
            doAgain = input("Do you take the goblin up on his offer?(y/n): ")
            if doAgain == "y":
                print("\nYou reset the game, and the goblin places an even bigger pile of winnings on the table.")
                flag6 = False
            elif doAgain == "n":
                print('\n"Very well", the goblin says. "I know you will be back here soon anyway..."')
                print("You take your winnings and leave his table.")
                flag6 = False
            else:
                print("Invalid Input.")
    elif player2Wins == True:
        print(f"The goblin takes the {goldIn} Gold.")
        print("You lament the loss of your hard-earned gold, and return to the bar.")
        doAgain = "n"
    return doAgain, goldIn, player2Wins

def mainDiceGame(player1Name, player2Name):
    player1Score = 0
    player2Score = 0
    for i in range(0, 5):
        player1Dice1, player1Dice2, player2Dice1, player2Dice2 = diceOut(player1Name, player2Name)
        player1Score, player2Score = playerTurn(player1Dice1, player1Dice2, player2Dice1, player2Dice2, player1Score,
                                                player2Score, player1Name, player2Name)

    if player1Score > player2Score:
        print(f"\n{player1Name}'s score is larger than the goblin's score.")
        player1Wins = True
        player2Wins = False
    elif player2Score > player1Score:
        print(f"\nThe goblin's score is larger than {player1Name}'s score.")
        player2Wins = True
        player1Wins = False
    elif player2Score == player1Score:
        flag1 = True
        while flag1 == True:
            p1Die = random.randint(1, 6)
            print(f"{player1Name}'s die is: {p1Die}")
            p2Die = random.randint(1, 6)
            print(f"The goblin's die is: {p2Die}")
            if p1Die > p2Die:
                print(f"\n{player1Name}'s die is larger than the goblin's die.")
                player1Wins = True
                flag1 = False
            elif p2Die > p1Die:
                print(f"\nThe goblin's die is larger than {player1Name}'s die.")
                player2Wins = True
                flag1 = False
            else:
                flag1 = True

    if player1Wins == True:
        print("Congratulations, you won!")
    elif player2Wins == True:
        print("You lost.")
        print("The goblin snatches the gold placed on the table and scurries away...")
    return player1Wins, player2Wins

def diceGame(player1Name, player2Name, goldIn):
    player1Wins, player2Wins = mainDiceGame(player1Name, player2Name)
    doAgain, goldIn, player2Wins = endGameIf(player1Wins, player2Wins, goldIn)
    return doAgain, goldIn, player2Wins