import random
import time

# Character class
class Character:
    lifePoints = 100
    def get_lifePoints(self):
        return self.lifePoints
    def set_lifePoints(self, lifePoints):
        self.lifePoints = lifePoints
    attackPoints = 10
    def get_attackPoints(self):
        return self.attackPoints
    def set_attackPoints(self, attackPoints):
        self.attackPoints = attackPoints
    def attack(self, target):
        target.set_lifePoints(target.get_lifePoints() - self.attackPoints)
        print("target have ", target.get_lifePoints(), " life points")

# Warrior class
class Warrior(Character):
    lifePoints = Character.lifePoints + 20
    def get_lifePoints(self):
        return self.lifePoints
    def set_lifePoints(self, lifePoints):
        self.lifePoints = lifePoints
    attackPoints = Character.attackPoints + 10
    def get_attackPoints(self):
        return self.attackPoints
    def set_attackPoints(self, attackPoints):
        self.attackPoints = attackPoints

# Wizard class
class Wizard(Character):
    lifePoints = Character.lifePoints
    def get_lifePoints(self):
        return self.lifePoints
    def set_lifePoints(self, lifePoints):
        self.lifePoints = lifePoints
    attackPoints = Character.attackPoints
    def get_attackPoints(self):
        return self.attackPoints
    def set_attackPoints(self, attackPoints):
        self.attackPoints = attackPoints
    def drinkPotion(self):
        self.lifePoints += 15

def game():
    player1 = Warrior()
    player2 = Wizard()
    while player1.lifePoints >= 0 or player2.lifePoints >= 0:
        player1.attack(player2)
        time.sleep(1)
        player2.attack(player1)
        time.sleep(1)


if __name__ == "__main__":
    game()
    

    #if Warrior.lifePoints == 0:
    #    print("Warrior loose")
    #elif Wizard.lifePoints == 0:
    #    print("Wizard loose")
    #else:
    #    warriorDamage()
    #    time.sleep(1)
    #    wizardDamage()
    #    time.sleep(1)
 