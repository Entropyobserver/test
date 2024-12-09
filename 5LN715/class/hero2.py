class Hero:
    def __init__(self, name, health, weapon, enemies = 0):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.enmies = enemies
        
    def is_of_age(age):
        if age > 18:
            return True
        return False


hero1 = Hero( 75, "Sword", 104)
hero2 = Hero( 100, "Knife", 15)


print(hero2.is_of_age(11)) 