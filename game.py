import random
import time

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

def warriorDamage():
    ratioDmg = random.randint(1,10)/10
    Dmg = Warrior.attackPoints * ratioDmg
    attack = Wizard.set_lifePoints - Dmg
    print(Wizard.get_lifePoints)
    return attack

def wizardDamage():
    ratioDmg = random.randint(1,10)/10
    Dmg = Wizard.attackPoints * ratioDmg
    attack = Warrior.set_lifePoints - Dmg
    print(Warrior.get_lifePoints)
    return attack

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
