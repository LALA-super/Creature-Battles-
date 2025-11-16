import random #importing random in order have acces to the probability and chance of the fucntion

#king class
class creature:
    def __init__(self, name, energy, HP, ATK):
        self.name = name
        self.energy = energy
        self.HP = HP
        self.ATK = ATK

    def __str__(self):
        return f" {self.name} - ENG: {self.energy} - HP: {self.HP} - ATK: {self.ATK}"
   
    def current_status(self):
        return f"{self.name} has: {self.HP} HP | {self.energy} Energy |  {self.ATK} ATK" #so that when instancing, we can choose to print and show how each creature is currently doing

    def __sub__(self, other):
        other.energy -= self.ATK
        if other.energy < 0:
            other.energy = 0
            return f"{other.name} is defeated"
        return f"{self.name} attacks {other.name} for {self.ATK} damage!"
    
    def __add__(self, val):
        self.energy += val
        other.energy -= self.ATK
        return f"{self.name} recovers {val} energy, total energy is now {self.ENG} ENG!"
 


    def __mul__(self, factor):
        self.ATK = int(self.ATK * factor)
        return f"{self.name} trained. their ATK is now; {self.ATK}"
   
        

#knight 1 class 
class elemental(creature):
    def __init__(self, name, energy, HP, ATK, MANA):
        self.name = name
        self.energy = energy
        self.HP = HP
        self.ATK = ATK
        self.MANA = MANA
    def __str__(self):
        return f"{self.name} | HP: {self.HP} | Energy: {self.energy} | ATK: {self.ATK} | MANA: {self.MANA}"#mana is a ATK booster, for every attack there is a small bonus damage that an elemental can do
   


    def __sub__(self, other):
       base_damage = self.ATK
       manabonus = 0
       manaused = False

       if self.MANA >= 10:
          manabonus = int(self.ATK * 0.5)
          self.MANA -= 10
          manaused = True
      
       if self.MANA < 0:
        self.MANA = 0

        
       totaldmg = base_damage + manabonus
       other.HP -= totaldmg
       
       if manaused:
            manatracker = "(used 10 mana for bonus damage)" 
       else:
            manatracker = ""

       return f"{self.name} damages {other.name} for {totaldmg}, {manatracker}"
        


#knight 2 class
class draugr(creature):
    def __init__(self, name, energy, HP, ATK, CORR):
        self.name = name
        self.energy = energy
        self.HP = HP
        self.ATK = ATK
        self.CORR = CORR
    def __str__(self):
        return f"{self.name} | HP: {self.HP} | Energy: {self.energy} | ATK: {self.ATK} | CORROSION: {self.CORR}"#corrosion is a feature where the undead draugr takes damage each turn/action it does, so draugrs have to end fights quick and cant risk being in prolonged battles.

    def __sub__(self, other):
        if self.energy <= 0:
            return f"{self.name} is too exhausted to move."
        other.HP -= self.ATK
        self.energy -= 10
    
        self_damage = int(self.CORR * 0.1)
        self.HP -= self_damage
        self.CORR += 2
    
        if self.HP < 0:
            self.HP = 0
        if other.HP < 0:
            other.HP = 0
            return f"{self.name} attacks at {other.name}"
        return f"{self.name} suffers {self_damage} corrosion damage!"




#knight 3 class
class angel(creature):
    def __init__(self, name, energy, HP, ATK, Faith):
        self.name = name
        self.energy = energy
        self.HP = HP
        self.ATK = ATK
        self.Faith = Faith
    def __str__(self):
        return f"{self.name} | HP: {self.HP} | Energy: {self.energy} | ATK: {self.ATK} | Faith: {self.Faith}" #faith is a luck attribute, every turn that an angel performs, there is a chance that they recieve some form of effect
   
    def __add__(self, value):
        buff = value + int(self.Faith / 10)
        self.HP += buff
        if self.HP > 200:
            self.HP = 200
            return f"{self.name} recieves a miracle and gains {buff} HP"
            
        chance = random.random(1, 100) #using the random function allows for a probability of chance for the angels faith, so if an angel plays smart, they can last for a long time in a battle, as there is chances that they get healed and stamina boosted
       
       #below are all the different effects that faith can provide,
        if chance <= self.Faith * 0.3: 
            effect = random.choice(["divine_light", "blessed_shield", "miracle"])
        if effect == "divine_light":
            self.ATK += 10
            return f"{self.name}'s prayer summons Scorching Divinivty, their ATK is increased!"
       
        elif effect == "blessed_shield":
                print(f"{self.name} is blessed by their God, their energy is fully restored!")
                self.energy = 100
       
        elif effect == "miracle":
                print(f"{self.name}'s body shines, their HP is restored!")
                self.HP = 200
        else:
            return f"{self.name}'s faith is ignored."


#instancing the classes and defining their attributes and values
elemental1 = elemental("Frig",12,80,8,93)
print(str(elemental1))
draugr1 = draugr("Palair",10,90,12,40)
print(str(draugr1))
angel1 = angel("Vena",18,100,10,240)
print(str(angel1))

print("GAME BEGIN")

#each of the following is an example of all the different kinds of attacks, first one being elemental attacks draugr and so on. this is done to test that all attributes work
print(elemental1 - draugr1)
print(elemental1.current_status())
print(draugr1.current_status())

print(elemental1 - angel1)
print(elemental1.current_status())
print(angel1.current_status())

print(angel1 - draugr1)
print(angel1.current_status())
print(draugr1.current_status())

print(angel1 - elemental1)
print(angel1.current_status())
print(elemental1.current_status())


print(draugr1 - elemental1)
print(draugr1.current_status())
print(elemental1.current_status())

print(draugr1 - angel1)
print(draugr1.current_status())
print(angel1.current_status())
