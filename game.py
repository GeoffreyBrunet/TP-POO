import classes_TP
import random
import time

def launch():
    player1 = classes_TP.Warrior()
    player2 = classes_TP.Wizard()
    print("player 1 have ", player1.lifePoints ," life points")
    print("player 2 have ", player2.lifePoints ," life points")
    if player1.lifePoints > 0 or player2.lifePoints > 0:
        print("It's Warrior turn !")
        player1.attack(player2)
        selfHit = random.randint(1,5)
        getHeal = random.randint(1,2)
        print("Warrior have", player1.lifePoints, " life points")
        time.sleep(1)
        print("It's Wizard turn !")
        player2.attack(player1)
        player2.drinkPotion()
        print("Wizard have", player1.lifePoints, " life points")
        time.sleep(1)
    else:
        print("loose")


if __name__ == "__main__":
    launch()
