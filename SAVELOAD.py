from PATHS import *
import pickle
"""
.save_character(x)
.load_character(x)
.save_world(x)
.load_character(x)
"""

_PATH = PATH()

class SL(object):
    def __init__(self):
        self.dummy = None
        
    def save_character(self, character):
        nameWpath = _PATH.character(character.getName())
        with open(nameWpath, 'wb') as _file: 
            pickle.dump(character, _file, pickle.HIGHEST_PROTOCOL)

    def load_character(self, charname):
        try:
            nameWpath = _PATH.character(charname)
            with open(nameWpath, 'rb') as _file: #load by charname.getID instead of getName()
                character = pickle.load(_file)
        except FileNotFoundError:
            ask = input('Try again?[y/n]')
            if ask == 'y':
                charname = input("Enter your character name again: ")
                character = load_character(charname)
            else:
                print('LOAD FAIL!')
                character = 'LOAD FAIL!'
        return character

    def save_world(self, world):
        nameWpath = _PATH.world(world.getName()) #save as 
        with open(nameWpath, 'wb') as _file:
            pickle.dump(world, _file, pickle.HIGHEST_PROTOCOL)

    def load_world(self, worldname):
        try:
            nameWpath = _PATH.world(worldname) #load as
            with open(nameWpath, 'rb') as _file:
                world = pickle.load(_file)
                world.getStat()
        except FileNotFoundError:
            world = None
        return world

    
