import random

class Weapon(object):
    def __init__(self):
        self.ID = 0
        self.type = ''
        self.name = ''
        self.level = 1
        self.buff = 0

    def getName(self):
        return self.name

    def getBuff(self):
        return self.buff

    def getID(self):
        return self.ID

    def _repr(self):
        print('Type {0} Name {1} ID {2} Buff {3}'.format(self.type,self.name,self.ID,self.buff)) 

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

    def setID(self, val):
        self.ID = val

class Potion(object):
    def __init__(self, _type):
        self.ID = 0
        self.type = _type
        self.name = 'Potion'
        if _type==0:
            self.color = 'red'
        elif _type==1:
            self.color = 'blue'
        self.buff = 0.8

    def _repr(self):
        print('Type {0} Name {1} ID {2} Buff {3} Color {4}'.format(self.type,self.name,self.ID,self.buff,self.color))

    def getType(self):
        return self.type

    def getBuff(self):
        return self.buff

    def getName(self):
        return self.name

    def getID(self):
        return self.ID

    def setID(self, val):
        self.ID = val

    def setName(self, val):
        self.name = val
    
class Consumable(object):
    def __init(self):
        self.name = 'Consumables'
        self.ID = 0
        self.type = 0
        self.buff = 0
        self.target= ''
        
    def _repr(self):
        print('Type {0} Name {1] ID {2} Buff {3}'.format(self.type,self.name,self.ID,self.buff))

    def updateTarget(self):
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

    def getID(self):
        return self.ID

    def setID(self, val):
        self.ID = val

    def setName(self, val):
        self.name = val

    def setType(self, val):
        """ Enchence code
        1 - rock
        2 - scissor
        3 - paper
        4 - shield
        5 - hp
        6 - mana
        """
        self.type = val
        self.updateTarget()

    def setBuff(self, val):
        self.buff=val
        
        
            
    
