# абстрактный класс для оружия
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
        
# конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print("Боец без оружия!")

# Реализация боя
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")

def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()

# Пример использования
fighter = Fighter("Герой")
monster = Monster("Злобный монстр")

# Боец выбирает меч
fighter.change_weapon(Sword())
battle(fighter, monster)

# Боец выбирает лук
fighter.change_weapon(Bow())
battle(fighter, monster)
