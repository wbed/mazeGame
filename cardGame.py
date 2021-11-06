import random

#CARD GAME
def makeDeck():
    cardDeck = [['Black', 1], ['Black', 2], ['Black', 3], ['Black', 4], ['Black', 5], ['Black', 6], ['Black', 7],
                ['Black', 8], ['Black', 9], ['Black', 10],
                ['Red', 1], ['Red', 2], ['Red', 3], ['Red', 4], ['Red', 5], ['Red', 6], ['Red', 7], ['Red', 8],
                ['Red', 9], ['Red', 10],
                ['Yellow', 1], ['Yellow', 2], ['Yellow', 3], ['Yellow', 4], ['Yellow', 5], ['Yellow', 6], ['Yellow', 7],
                ['Yellow', 8], ['Yellow', 9], ['Yellow', 10]]
    random.shuffle(cardDeck)
    return cardDeck

def cardMessage(player1Name, player2Name, player1Card, player2Card):
    print(f"{player1Name}'s card: {player1Card[0]} {player1Card[1]}.")
    print(f"The goblin's card: {player2Card[0]} {player2Card[1]}.")


def takeCards(cardDeck, player1Name, player2Name):
    player1Deck = []
    player2Deck = []
    for i in range(0, 30, 2):
        input("Draw another card: ")
        print("")
        p1Win = False
        p2Win = False
        player1Card = cardDeck[i]
        player2Card = cardDeck[i + 1]
        if (player1Card[0] == 'Red') and (player2Card[0] == 'Black'):
            cardMessage(player1Name, player2Name, player1Card, player2Card)
            print(f"{player1Name}'s card beat the goblin's card.")
            p1Win = True
        elif (player1Card[0] == 'Yellow') and (player2Card[0] == 'Red'):
            cardMessage(player1Name, player2Name, player1Card, player2Card)
            print(f"{player1Name}'s card beat the goblin's card.")
            p1Win = True
        elif (player1Card[0] == 'Black') and (player2Card[0] == 'Yellow'):
            cardMessage(player1Name, player2Name, player1Card, player2Card)
            print(f"{player1Name}'s card beat the goblin's card.")
            p1Win = True
        elif (player2Card[0] == 'Red') and (player1Card[0] == 'Black'):
            cardMessage(player1Name, player2Name, player1Card, player2Card)
            print(f"The goblin's card beat {player1Name}'s card.")
            p2Win = True
        elif (player2Card[0] == 'Yellow') and (player1Card[0] == 'Red'):
            cardMessage(player1Name, player2Name, player1Card, player2Card)
            print(f"The goblin's card beat {player1Name}'s card.")
            p2Win = True
        elif (player2Card[0] == 'Black') and (player1Card[0] == 'Yellow'):
            cardMessage(player1Name, player2Name, player1Card, player2Card)
            print(f"The goblin's card beat {player1Name}'s card.")
            p2Win = True
        elif player2Card[0] == player1Card[0]:
            cardMessage(player1Name, player2Name, player1Card, player2Card)
            if player1Card[1] > player2Card[1]:
                print(f"{player1Name}'s card beat the goblin's card.")
                p1Win = True
            elif player1Card[1] < player2Card[1]:
                print(f"The goblin's card beat {player1Name}'s card.")
                p2Win = True

        if p1Win == True:
            player1Deck.append(player1Card)
            player1Deck.append(player2Card)
        elif p2Win == True:
            player2Deck.append(player1Card)
            player2Deck.append(player2Card)

    player1Length = len(player1Deck)
    player2Length = len(player2Deck)
    player1Wins = False
    player2Wins = False

    if player1Length > player2Length:
        print("\nCongratulations, you won!")
        print(f"You collected {player1Length} cards.")
        print(f"The goblin collected {player2Length} cards.")
        player1Wins = True
        winnerLength = player1Length
    elif player2Length > player1Length:
        print("\nYou lost.")
        print(f"The goblin collected {player2Length} cards and won.")
        print(f"He mischievously grins as he pockets your money...")
        player2Wins = True
        winnerLength = player2Length

    if player1Wins == True:
        winnerName = player1Name
    elif player2Wins == True:
        winnerName = "The goblin"
    return winnerName, winnerLength, player1Wins, player2Wins

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

def cardGame(player1Name, player2Name, goldIn):
    cardDeck = makeDeck()
    winnerName, winnerLength, player1Wins, player2Wins = takeCards(cardDeck, player1Name, player2Name)
    doAgain, goldIn, player2Wins = endGameIf(player1Wins, player2Wins, goldIn)
    return doAgain, goldIn, player2Wins