"""VARAIBLES
    1) hammer, scissor, bag are weapons can be use to attack and defend
    ***RULE ===> hammer > scissor, scissor > bag, bag > hammer***
    ***RULE ===> shield blocks patial damage from hammer, scissor, bag
    2) appid use for save games
    3) gold use for purchasing in-game
    4) speed use to decide who is going to attack first (5-10)
"""

"""FUNCTIONS
    get*variables*()
    set*variables*(value)
    inc*variables*(value)
"""
import random

class Character(object):
    def __init__(self, name):
        """name"""
        self.name = name
        self.id = 0

        """weapon stats"""
        self.rock = 20
        self.scissor = 20
        self.paper = 20
        self.shield = 10

        """related stats"""
        self.hp = 100
        self.level = 1
        self.exp = 0
        self.current_max_exp = 100
        self.next_max_exp = 200
        self.base_exp = 100
        self.speed = 5
        self.gold = 0

    """EXP system"""
    #level up if exp exceed current level exp
    #multi-level up when the exp gained greater than more than 1 level exp limits
    def power_up(self):
        self.incRock((self.rock/100)*15)
        self.incScissor((self.scissor/100)*15)
        self.incPaper((self.paper/100)*15)
    
    def level_up(self):
        self.level+=1
        self.current_max_exp = self.next_max_exp
        self.next_max_exp = self.current_max_exp+self.base_exp * self.level #formula
        if self.exp>=self.current_max_exp:
            self.level_up()
            self.power_up()
        
    def gainExp(self, value):
        self.exp+=value
        if self.exp >= self.current_max_exp:
            self.level_up()

    def bounty(self):
        bounty_exp = random.randint(18, 22)
        if self.exp>150:
            amount = (self.exp/100)*20
            minimum = amount-(amount/100*5)
            maximum = amount+(amount/100*5)
            bounty_exp = random.randint(minimum, maximum)
        return bounty_exp
            
    """
    All the GET functions go here
    """
    def _repr(self):
        print(self.name)
        print("Rock {0} Scissor {1} Paper {2}".format(self.rock, self.scissor, self.paper))
        print("ID {0} Gold {1} Hp {2} Exp {3} Lev{4}".format(self.id, self.gold, self.hp, self.exp, self.level))        

    def getLevel(self):
        return self.level
    
    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def getRock(self):
        return self.rock

    def getScissor(self):
        return self.scissor

    def getPaper(self):
        return self.paper

    def getWeapon(self, choice):
        if choice==0:
            result = self.rock
        elif choice==1:
            result = self.scissor
        elif choice==2:
            result = self.paper
        return result

    def getShield(self):
        return self.shield
    
    def getID(self):
        return self.id

    def getGold(self):
        return self.gold

    def getHp(self):
        return self.hp

    def getExp(self):
        return self.exp

    """
    All the SET functions go here
    """
    def setName(self, value):
        self.name = value

    def setSpeed(self, value):
        self.speed = value

    def setRock(self, value):
        self.rock = value

    def setScissor(self, value):
        self.scissor = value

    def setPaper(self, value):
        self.paper = value

    def setDamAll(self, low, high):
        self.rock = random.randint(low, high)
        self.scissor = random.randint(low, high)
        self.paper = random.randint(low, high)

    def setShield(self, value):
        self.shield = value

    def setHp(self, value):
        self.hp = value

    def setID(self, value):
        self.id = value

    def setExp(self, value): #developer only
        self.exp=value

    """
    All the INCREASE function go here
    """
    def incSpeed(self, value):
        self.speed+=value

    def incRock(self, value):
        self.rock+=value

    def incScissor(self, value):
        self.scissor+=value

    def incPaper(self, value):
        self.paper+=value

    def incShield(self, value):
        self.shield+=value

    def incHp(self, value):
        self.hp+=value

    def incExp(self, value):
        self.exp+=value
        if self.exp >= self.current_max_exp:
            level_up()

    def incLevel(self, value):
        self.level+=value

    """bots function ONLY"""
    def random_choice(self):
        return random.randint(0, 2)
    
    def random_weapon(self):
        choice = random.randint(0, 2)
        if choice==0:
            result = 'rock'
        elif choice==1:
            result = 'scissor'
        elif choice==2:
            result = 'paper'
        return result

