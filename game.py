import classes_TP
import random
import time

class launchGame:
    #function for start a game
    def launch(self):
        player1 = classes_TP.Warrior()
        player2 = classes_TP.Wizard()
        print("player 1 have ", player1.lifePoints ," life points")
        print("player 2 have ", player2.lifePoints ," life points")
        while player1.get_lifePoints() > 0 and player2.get_lifePoints() > 0:
            print("It's Warrior turn !")
            player1.attack(player2)
            selfHit = random.randint(1,5)
            getHeal = random.randint(1,2)
            print("Warrior Attack ! Wizard have have", player1.lifePoints, " life points")
            time.sleep(1)
            print("It's Wizard turn !")
            player2.attack(player1)
            player2.drinkPotion()
            print("Warrior launch a spell ! Warrior have", player2.lifePoints, " life points")
            time.sleep(1)
        if player1.lifePoints <= 0:
            print("Warrior loose")
            player1.warriorVictory += 1
            return player1.warriorVictory
        elif player2.lifePoints <= 0:
            print("Wizard loose")
            player2.wizardVictory += 1
            return player1.warriorVictory
        else:
            print("Suicide, equality, we don't know ! That fight was incredible !")
        print("Game is now finished. want retry?")
        restartGame()

    def restartGame(self):
        play = input("Y: Yes, N: No, Choose: ")
        if play == "Y" or play == "y":
            game.launch()
        else:
            print("By by, have a nice week!")
            time.sleep(1)
            exit()