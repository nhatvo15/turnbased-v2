import random

class Weapon(object):
    def __init__(self):
        self.type = ''
        self.name = ''
        self.level = 1
        self.buff = 0

    def getName(self):
        return self.name

    def getBuff(self):
        return self.buff

    def _repr(self):
        print('Type {0} Name {1} Buff: {2}'.format(self.type, self.name, self.buff)) 

    def updateBuff(self):
        self.buff = (10*self.level)/100

    def setType(self, val):
        self.type = val

    def setName(self, val):
        self.name = val

    def setLevel(self, val):
        self.level = val
        self.updateBuff()

    def setBuff(self, val):
        self.buff = val

class Potion(object):
    def __init__(self, _type):
        self.type = _type
        self.name = 'Potion'
        if _type==0:
            self.color = 'red'
        elif _type==1:
            self.color = 'blue'
        self.buff = 0.8

    def _repr(self):
        print('Type {0} Buff {1} Color {2}'.format(self.type, self.buff, self.color))

    def getType(self):
        return self.type

    def getBuff(self):
        return self.buff

    def getName(self):
        return self.name
    
class Consumable(object):
    """ Enchence code
    1 - rock
    2 - scissor
    3 - paper
    4 - shield
    5 - hp
    6 - mana
    """
    def __init(self, _type, _buff):
        self.type = _type
        self.buff = _buff
        self.name = 'Consumables'
        if self.type==1:
            self.target = 'rock'
        elif self.type==2:
            self.target = 'scissor'
        elif self.type==3:
            self.target = 'paper'
        elif self.type==4:
            self.target = 'shield'
        elif self.type==5:
            self.target = 'hp consumable'
        elif self.type==6:
            self.target = 'mana consumable'

    def getType(self):
        return self.type

    def getBuff(self):
        return self.buff

    def getName(self):
        return self.name
            
    
