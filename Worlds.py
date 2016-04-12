from Character import *
import random

"""
import items
this feature support mods who can drop out/sell item which quality depends on
chances and the difficulty of the world
"""
##################################
#                                #
#          MONSTER NAMES         #
#                                #
##################################
MONSTER_NAMES_LIST = ('CLEMENTINE', 'BLACKBERRY', 'SATSUMA', 'PAPAYA',
                       'APPLE', 'TOMATO', 'HONEYDEW', 'MANGO', 'GRAPEFRUIT',
                       'APRICOT', 'AVOCADO', 'LIME', 'TANGERINE', 'HUCKLEBERRY',
                       'POMEGRANATE', 'NECTARINE', 'GUAVA', 'KUMQUAT', 'COCONUT',
                       )
LENGTH_NAMES = len(MONSTER_NAMES_LIST) - 1

##################################
#                                #
# GLOBAL VARAIBLE FOR            #
#     DAMAGE DEPENDS ON LEVEL    #
#                                #
##################################

LEV1_LOW, LEV1_HIGH = 10, 15 #lv1
LEV2_LOW, LEV2_HIGH = 15, 20 #lv2
LEV3_LOW, LEV3_HIGH = 20, 25 #lv3
LEV4_LOW, LEV4_HIGH = 25, 30 #lv4



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
        self.size = "small"
        self.mob1 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob1
        self.mob2 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob2
        self.mob3 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob3
        self.boss = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]+" ELITE") #boss
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
        print("Statistic: ")
        print("Name:{0} Size:{1} Level:{2}".format(self.name, self.size, self.lev))
        self.mob1._repr()
        self.mob2._repr()
        self.mob3._repr()
        self.boss._repr()
        
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
class World_medium(object):
    def __init__(self, name, level):
        """name"""
        self.name = name
        self.lev = level
        self.size = "medium"
        self.mob1 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob1
        self.mob2 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob2
        self.mob3 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob3
        self.mob4 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob4
        self.mob5 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob5
        self.boss = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]+" ELITE") #boss
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
        print("Statistic: ")
        print("Name:{0} Size:{1} Level:{2}".format(self.name, self.size, self.lev))
        self.mob1._repr()
        self.mob2._repr()
        self.mob3._repr()
        self.mob4._repr()
        self.mob5._repr()
        self.boss._repr()
        
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
class World_big(object):
    def __init__(self, name, level):
        """name"""
        self.name = name
        self.lev = level
        self.size = "big"
        self.mob1 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob1
        self.mob2 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob2
        self.mob3 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob3
        self.mob4 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob4
        self.mob5 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob5
        self.mob6 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob6
        self.mob7 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]) #mob7
        self.boss1 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]+" ELITE") #boss1
        self.boss2 = Character(MONSTER_NAMES_LIST[random.randint(0, LENGTH_NAMES)]+" ELITE") #boss2
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
        print("Statistic: ")
        print("Name:{0} Size:{1} Level:{2}".format(self.name, self.size, self.lev))
        self.mob1._repr()
        self.mob2._repr()
        self.mob3._repr()
        self.mob4._repr()
        self.mob5._repr()
        self.mob6._repr()
        self.mob7._repr()
        self.boss1._repr()
        self.boss2._repr()
        
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
    
        
