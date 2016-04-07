from Character import *
import random

"""
import items
this feature support mods who can drop out/sell item which quality depends on
chances and the difficulty of the world
"""

class World(object):
    def __init__(self, name):
        """name"""
        self.name = name
        self.mob1 = Character("Monkey")
        self.mob2 = Character("Tiger")
        self.mob3 = Character("Snake")
        self.boss = Character("Panda")
        
        
        """
        self.dif = dif
        #Define the size of the world
        #There are 2 sizes: small(1) and big(2)
        #(1) has 3 mobs + 1 boss
        #(2) has 6 mobs + 1 boss
        self.size = size

        """ """
        if self.size == 1:
            self.numMob = 3
            self.numBoss = 1
            self.numNPC = 0
        elif self.size == 2:
            self.numMob = 6
            self.numBoss = 1
            self.numNPC = 1
        #can be added for more!  expansion??
        """

    def getStat(self):
        print("""Return statistic of this world
              include: how many mobs left unkilled, NPC left undiscovered""")

    def getName(self):
        return self.name
    """
    def getSize(self):
        return self.size

    def getDif(self):
        return self.dif
    """

    def getMob1(self):
        return self.mob1

    def getMob2(self):
        return self.mob2

    def getMob3(self):
        return self.mob3

    def getBoss(self):
        return self.boss

    def setMob1(self, mob):
        self.mob1 = mob

    def setMob2(self, mob):
        self.mob2 = mob

    def setMob3(self, mob):
        self.mob3 = mob

    def setBoss(self, boss):
        self.Boss = boss
    
        
