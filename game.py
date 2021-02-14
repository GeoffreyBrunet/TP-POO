import classes_TP
import random
import time

class launchGame:
    def launch(self):
        player1 = classes_TP.Warrior()
        player2 = classes_TP.Wizard()
        print("player 1 have ", player1.lifePoints ," life points")
        print("player 2 have ", player2.lifePoints ," life points")
        while player1.get_lifePoints() >= 0 or not player2.get_lifePoints() >= 0:
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
        print("loose")
