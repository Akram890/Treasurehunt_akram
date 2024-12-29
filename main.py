class Character:
    def __init__ (self,name,weapon):
        self.name=name
        self.weapon=weapon
    def set_details(self,name,weapon):
        self.name=name
        self.weapon=weapon
    def attack(self):  
        return f"{self.name} attacks with {self.weapon.use()}"  
class Weapon:  
    def __init__(self, name, type_of_weapon, damage, range, special_ability):  
        self.name = name  
        self.type_of_weapon = type_of_weapon  
        self.damage = damage  
        self.range = range  
        self.special_ability = special_ability  
    def use(self):  
        return f"{self.name} used! Deals {self.damage} damage." + (f" Special Ability: {self.special_ability}" if self.special_ability else "") 

class Player(Character):
    def __init__ (self,name,weapon):
       super().__init__(name,weapon)
       self.health=100
       self.strength=350
       self.inventory=[]
       self.level=1
    def set_details(self):
       self.health=100
       self.strength=350
       self.inventory=[]
    def level_up(self,amount=2):
        self.level += amount
        print(f"{self.name} has leveled to level {self.level} ")
    def attack(self):  
        base_attack = super().attack()  
        return f"{base_attack} (Level: {self.level})"  
    def check_defeat(self, player):  
        if self.health <= 0:  
            print(f"{self.name} has been defeated!")  
            player.level_up()   
            self.health = 100  
    def take_damage(self, damage, player):  
        self.health -= damage  
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")  
        self.check_defeat(player) 
    def pick_up(self):
        self.inventory.append(item)
        

     
class SoldierVillain(Character):
    def __init__ (self,name,weapon):
       super().__init__(name,weapon)
       self.health=75
       self.strength=220
    def set_details(self):
       self.health=100
       self.strength=350
    def attack(self):  
        base_attack = super().attack()  
        return f"{base_attack} (Level: {self.level})"  
    def check_defeat(self, player):  
        if self.health <= 0:  
            print(f"{self.name} has been defeated!")  
            player.level_up()   
            self.health = 100  
    def take_damage(self, damage, player):  
        self.health -= damage  
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")  
        self.check_defeat(player)  

class item:  
    def __init__(self, name, description, special_ability):  
        self.name = name
        self.description=description
        self.special_ability=  special_ability
    def __str__(self):  
        return f"{self.name}: {self.description}:{self.special_ability}"  

    



    
       


    
