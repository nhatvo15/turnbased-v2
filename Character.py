"""VARAIBLES
    1) hammer, scissor, bag are weapons can be use to attack and defend
    ***RULE ===> hammer > sword, sword > shield, shield > hammer***
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
        self.id = random.randint(9999, 100000)

        """weapon stats"""
        self.hammer = 20
        self.scissor = 20
        self.bag = 20
        self.shield = 10

        """related stats"""
        self.hp = 100
        self.exp = 0
        self.speed = 5
        self.gold = 0

    """
    All the GET functions go here
    """
    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def getHammer(self):
        return self.hammer

    def getScissor(self):
        return self.scissor

    def getBag(self):
        return self.bag

    def getShield(self):
        return self.shield
    
    def getAppid(self):
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

    def setHammer(self, value):
        self.hammer = value

    def setScissor(self, value):
        self.scissor = value

    def setShield(self, value):
        self.shield = value

    def setBag(self, value):
        self.bag = value

    def setHp(self, value):
        self.hp = value

    """
    All the INCREASE function go here
    """
    def incSpeed(self, value):
        self.speed+=value

    def incHammer(self, value):
        self.hammer+=value

    def incScissor(self, value):
        self.scissor+=value

    def incBag(self, value):
        self.bag+=value

    def incShield(self, value):
        self.shield+=value

    def incHp(self, value):
        self.Hp+=value

    def incExp(self, value):
        self.exp+=value

