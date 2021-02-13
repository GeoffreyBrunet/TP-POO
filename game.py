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
        ratioDmg = random.randint(1,10)/10
        target.set_lifePoints(target.get_lifePoints() - self.attackPoints * ratioDmg)
        print("target have ", target.get_lifePoints(), " lp")

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
    def selfHit(self):
        ratioDmg = random.randint(1,10)/10
        self.set_lifePoints(self.get_lifePoints() - self.attackPoints * ratioDmg)

# Wizard class
class Wizard(Character):
    lifePoints = Character.lifePoints
    potion = 5
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
        potion -= 5
        print("Healed ! You have ", potion, "potions.")

def game():
    player1 = Warrior()
    player2 = Wizard()
    print("player 1 have ", player1.lifePoints ," life points")
    print("player 1 have ", player1.lifePoints ," life points")
    if player1.lifePoints >= 0 or player2.lifePoints >= 0:
        player1.attack(player2)
        selfHit = random.randint(1,5)
        getHeal = random.randint(1,2)
        if selfHit == 1:
            print("truc ici")
        else:
            print("don't self hit")
        time.sleep(1)
        player2.attack(player1)
        if getHeal == 1:
            player2.drinkPotion()
        else:
            print("don't self heal")
        time.sleep(1)
    else:
        print("loose")


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
 