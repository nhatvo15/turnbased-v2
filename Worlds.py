from Character import *
import random

"""
import items
this feature support mods who can drop out/sell item which quality depends on
chances and the difficulty of the world
"""

##################################
# GLOBAL VARAIBLE FOR            #
#     DAMAGE DEPENDS ON LEVEL    #
##################################
LEV1_LOW, LEV1_HIGH = 10, 15
LEV2_LOW, LEV2_HIGH = 15, 20
LEV3_LOW, LEV3_HIGH = 20, 25
LEV4_LOW, LEV4_HIGH = 25, 30



##################################
#                                #
#         SMALL WORLD            #
#                                #
##################################
class World_small(object):
    def __init__(self, name, level):
        """name"""
        self.name = name
        self.lev = level
        self.mob1 = Character("mob1")
        self.mob2 = Character("mob2")
        self.mob3 = Character("mob3")
        self.boss = Character("boss")
        if self.lev==1:
            self.mob1.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob2.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob3.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.boss.setDamAll(LEV1_LOW+3, LEV1_HIGH+3)
        elif self.lev==2:
            self.mob1.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob2.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob3.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.boss.setDamAll(LEV2_LOW+3, LEV2_HIGH+3)
        elif self.lev==3:
            self.mob1.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob2.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob3.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.boss.setDamAll(LEV3_LOW+3, LEV3_HIGH+3)
        elif self.lev==4:
            self.mob1.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob2.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob3.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.boss.setDamAll(LEV4_LOW+3, LEV4_HIGH+3)
        

    def getStat(self):
        print("""Return statistic of this world
              include: how many mobs left unkilled, NPC left undiscovered""")

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

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
        self.boss = boss




##################################
#                                #
#         MEDIUM WORLD           #
#                                #
##################################
def World_medium(object):
    def __init__(self, name, level):
        """name"""
        self.name = name
        self.lev = level
        self.mob1 = Character("mob1")
        self.mob2 = Character("mob2")
        self.mob3 = Character("mob3")
        self.mob4 = Character("mob4")
        self.mob5 = Character("mob5")
        self.boss = Character("boss")
        if self.lev==1:
            self.mob1.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob2.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob3.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob4.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob5.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.boss.setDamAll(LEV1_LOW+3, LEV1_HIGH+3)
        elif self.lev==2:
            self.mob1.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob2.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob3.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob4.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob5.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.boss.setDamAll(LEV2_LOW+3, LEV2_HIGH+3)
        elif self.lev==3:
            self.mob1.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob2.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob3.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob4.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob5.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.boss.setDamAll(LEV3_LOW+3, LEV3_HIGH+3)
        elif self.lev==4:
            self.mob1.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob2.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob3.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob4.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob5.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.boss.setDamAll(LEV4_LOW+3, LEV4_HIGH+3)
        

    def getStat(self):
        print("""Return statistic of this world
              include: how many mobs left unkilled, NPC left undiscovered""")

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getMob1(self):
        return self.mob1

    def getMob2(self):
        return self.mob2

    def getMob3(self):
        return self.mob3

    def getMob4(self):
        return self.mob4

    def getMob5(self):
        return self.mob5

    def getBoss(self):
        return self.boss

    def setMob1(self, mob):
        self.mob1 = mob

    def setMob2(self, mob):
        self.mob2 = mob

    def setMob3(self, mob):
        self.mob3 = mob

    def setMob4(self, mob):
        self.mob4 = mob

    def setMob5(self, mob):
        self.mob5 = mob

    def setBoss(self, boss):
        self.boss = boss





##################################
#                                #
#           BIG WORLD            #
#                                #
##################################
def World_big(object):
    def __init__(self, name, level):
        """name"""
        self.name = name
        self.lev = level
        self.mob1 = Character("mob1")
        self.mob2 = Character("mob2")
        self.mob3 = Character("mob3")
        self.mob4 = Character("mob4")
        self.mob5 = Character("mob5")
        self.mob6 = Character("mob6")
        self.mob7 = Character("mob7")
        self.boss1 = Character("boss1")
        self.boss2 = Character("boss2")
        if self.lev==1:
            self.mob1.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob2.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob3.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob4.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob5.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob6.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.mob7.setDamAll(LEV1_LOW, LEV1_HIGH)
            self.boss1.setDamAll(LEV1_LOW+3, LEV1_HIGH+3)
            self.boss2.setDamAll(LEV1_LOW+3, LEV1_HIGH+3)
        elif self.lev==2:
            self.mob1.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob2.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob3.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob4.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob5.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob6.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.mob7.setDamAll(LEV2_LOW, LEV2_HIGH)
            self.boss1.setDamAll(LEV2_LOW+3, LEV2_HIGH+3)
            self.boss2.setDamAll(LEV2_LOW+3, LEV2_HIGH+3)
        elif self.lev==3:
            self.mob1.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob2.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob3.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob4.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob5.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob6.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.mob7.setDamAll(LEV3_LOW, LEV3_HIGH)
            self.boss1.setDamAll(LEV3_LOW+3, LEV3_HIGH+3)
            self.boss2.setDamAll(LEV3_LOW+3, LEV3_HIGH+3)
        elif self.lev==4:
            self.mob1.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob2.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob3.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob4.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob5.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob6.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.mob7.setDamAll(LEV4_LOW, LEV4_HIGH)
            self.boss1.setDamAll(LEV4_LOW+3, LEV4_HIGH+3)
            self.boss2.setDamAll(LEV4_LOW+3, LEV4_HIGH+3)        

    def getStat(self):
        print("""Return statistic of this world
              include: how many mobs left unkilled, NPC left undiscovered""")

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getMob1(self):
        return self.mob1

    def getMob2(self):
        return self.mob2

    def getMob3(self):
        return self.mob3

    def getMob4(self):
        return self.mob4

    def getMob5(self):
        return self.mob5

    def getMob6(self):
        return self.mob6

    def getMob7(self):
        return self.mob7

    def getBoss1(self):
        return self.boss1

    def getBoss2(self):
        return self.boss2

    def setMob1(self, mob):
        self.mob1 = mob

    def setMob2(self, mob):
        self.mob2 = mob

    def setMob3(self, mob):
        self.mob3 = mob

    def setMob4(self, mob):
        self.mob4 = mob

    def setMob5(self, mob):
        self.mob5 = mob

    def setMob6(self, mob):
        self.mob6 = mob

    def setMob7(self, mob):
        self.mob7 = mob

    def setBoss1(self, boss):
        self.boss1 = boss

    def setBoss2(self, boss):
        self.boss2 = boss
    
        
