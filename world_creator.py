from Worlds import *
import pickle

##############################
#                            #
#           Create           #
#                            #
##############################
def create_small(name, dif):
    ws = World_small(name, dif)
    return ws
1
def create_medium(name, dif):
    wm = World_medium(name, dif)
    return wm

def create_big(name, dif):
    wb = World_big(name, dif)
    return wb

##############################
#                            #
#           Save/Load        #
#                            #
##############################
def save(world):
    with open(world.getName()+'.world', 'wb') as _file:
        pickle.dump(world, _file, pickle.HIGHEST_PROTOCOL)

def load(worldname):
    try:
        with open(worldname+'.world', 'rb') as _file:
            world = pickle.load(_file)
            world.getStat()
    except FileNotFoundError:
        world = None
    return world


##############################
#                            #
# World Control Application  #
#                            #
##############################
def WCA():
    print("Welcome to World Control Application")
    choice=0
    while choice==0:
        choice=eval(input("CreateNew[1] Load[2] Exit[3]"))
        if choice==1: #New
            size=eval(input("S[1] M[2] L[3]"))
            if size==1: #small
                name, dif = map(str, input("new_name *space* lv(1-4)").split())
                dif=int(dif)
                world = create_small(name, dif)
            elif size==2: #medium
                name, dif = map(str, input("new_name *space* lv(1-4)").split())
                dif=int(dif)
                world = create_medium(name, dif)
            elif size==3: #large
                name, dif = map(str, input("new_name *space* lv(1-4)").split())
                dif=int(dif)
                world = create_big(name, dif)
            save(world) #saving

        elif choice==2: #Load
            while choice==2:
                name = input("load_name ")
                world = load(name)
                if world==None:
                    ask = input("World NOT FOUND/ Try again[y/n]: ")
                    if ask=='y':
                        continue
                    else:
                        choice=1
                else:
                    choice=0
        else:
             break

    world.getStat()

WCA()

                        

