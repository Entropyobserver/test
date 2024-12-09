class Hero:
    def __init__(self, name, health, weapon, enemies = 0):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.enmies = enemies

    @staticmethod
    def is_of_age(self, age):
        if age > 18:
            return True
        return False

# Creating instances of Hero
hero1 = Hero( 75, "Sword", 104)
hero2 = Hero( 100, "Knife", 15)

# Checking if hero2 is of age
print(hero2.is_of_age(11))  # Output: False
