import random

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
        getHit = random.randint(1,5)
        if getHit == 1:
            self.set_lifePoints(self.get_lifePoints() - self.attackPoints * ratioDmg)
            print("You hurt you, you have ", self.lifePoints, "lp.")
        else:
            print("Warrior don't hit himself.")

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
        potion = 5
        tryHeal = random.randint(1,2)
        if tryHeal == 1:
            self.lifePoints += 15
            potion -= 1
            print("Healed ! You have", potion, "potions.")
        else:
            print("Wizard don't heal himself.")
        
        
