import game
import time

game = game.launchGame()
warriorVictory = 0
wizardVictory = 0
# start game when main.py is started
if __name__ == "__main__":
    print("Want play to hero smash v1 ?")
    play = input("Y: Yes, N: No, Choose: ")
    if play == "Y" or play == "y":
        game.launch()
    else:
        print("By by, have a nice week!")
        time.sleep(1)
        exit()