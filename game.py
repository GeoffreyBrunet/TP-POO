import random
import time

class Character:
    lifePoints = 100
    actionPoints = 10

class Warrior(Character):
    lifePoints = Character.lifePoints + 20
    actionPoints = Character.actionPoints + 10

class Wizard(Character):
    lifePoints = Character.lifePoints
    actionPoints = Character.actionPoints
    def drinkPotion(self):
        self.lifePoints + 15

def warriorDamage():
    ratioDmg = random.randint(1,10)/10
    Dmg = ratioDmg
    return Dmg

def wizardDamage():
    ratioDmg = random.randint(1,10)/10
    Dmg = ratioDmg
    return Dmg

if __name__ == "__main__":
    if Warrior.lifePoints == 0:
        print("Warrior loose")
    elif Wizard.lifePoints == 0:
        print("Wizard loose")
    else:
        warriorDamage()
        time.sleep(1)
        wizardDamage()
        time.sleep(1)
