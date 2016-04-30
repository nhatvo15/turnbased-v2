from Worlds_Class import *
from PATHS import *
import pickle
import os.path
import glob

_PATH = PATH()

##############################
#                            #
#       Select World         #
#                            #
##############################
"""
Display a list of worlds in specific folder PATH
return the name of the selected world
"""
def display_list_world():
    print("Please select an existed world")
    print("==============================================")
    count = 1
    lw = {}
    worlds = glob.glob(_PATH.getPATH()+'*.world') #get all the file end with .world
    for w in worlds:
        w = w[49:] #cut the path
        w = w[:-6] #cut the tail (.world)
        lw[str(count)] = w #put them in an cataloged dictionary
        print(' '+str(count)
              +'. '+w+'\n') #print the name only
        count+=1
    print("==============================================")
    num = input(":= ")
    worldname = lw[str(num)]
    return worldname
    

##############################
#                            #
#      Load/Return World     #
#                            #
##############################
"""
Select/Load an existed world and return object world
"""
def load(worldname):
    try:
        nameWpath = _PATH.world(worldname) #load as
        with open(nameWpath, 'rb') as _file:
            world = pickle.load(_file)
    except FileNotFoundError:
        world = None
    return world



def World():
    worldname = display_list_world()
    world = load(worldname)
    world.getStat()
    return world

if __name__=="__World__":
    World()
