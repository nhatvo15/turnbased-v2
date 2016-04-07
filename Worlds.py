from Character import *
import random

"""
import items
this feature support mods who can drop out/sell item which quality depends on
chances and the difficulty of the world
"""

class World(object):
    def __init__(self, name, size, dif):
        """name"""
        self.name = name

        """difficulty"""
        self.dif = dif

        """size"""
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

    

        
