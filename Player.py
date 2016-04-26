from Character_Class import *
from PATHS import *
import pickle
import random
import os.path
import glob

_PATH = PATH()
#########################################
#                                       #
#            ID Functions               #
#                                       #
#########################################
"""   Support creating unique ID
"""
def makeID():
    _id = random.randint(99, 200)
    return _id

def checkID(val):
    data = open('id.txt', 'r')
    for line in data:
        words = line.split()
    temp = 0
    for item in words:
        if item == str(val):
            temp=1        
    data.close()
    return temp

def saveID(val):
    data = open('id.txt', 'a')
    data.write(str(val)+' ')
    data.close

def newID_validate():
    check = 1
    while check==1:
        userID = makeID()
        check = checkID(userID)
    return userID

#########################################
#                                       #
#          Character Functions          #
#                                       #
#########################################
def save_character(character):
    nameWpath = _PATH.character(character.getName())
    with open(nameWpath, 'wb') as _file: 
        pickle.dump(character, _file, pickle.HIGHEST_PROTOCOL)

def create_character():
    name = input("Enter character name:")
    character = Character(name) # create character
    userID = newID_validate() # create unique ID
    character.setID(userID) # set character ID = unique ID
    saveID(userID) # save userID on the text file
    save_character(character) #->save immediately
    return character

def load_character(charname):
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

##############################
#                            #
#  Select Existed Character  #
#                            #
##############################
"""
Display a list of characters in specific folder PATH
return the name of the selected character
"""
def display_list_character():
    print("Please select an existed character")
    print("==============================================")
    count = 1
    lw = {}
    worlds = glob.glob(_PATH.getPATH()+'*.character') #get all the file end with .world
    for w in worlds:
        w = w[49:] #cut the path
        w = w[:-10] #cut the tail (.world)
        lw[str(count)] = w #put them in an cataloged dictionary
        print(' '+str(count)
              +'. '+w+'\n') #print the name only
        count+=1
    print("==============================================")
    num = input(":= ")
    charname = lw[str(num)]
    return charname

########################################
#                                      #
#           MENU functions             #
#                                      #
########################################
def intro_menu():
    print("Welcome to the game!!!")
    opt = eval(input("New[1] Load[2] Exit[3]:"))
    if opt == 1:
        player = create_character() #->create
        print(player.getName())
        print("Greetings new comer", player.getName(), player.getID())
    elif opt == 2:
        charname = display_list_character()
        player = load_character(charname)
        print("We meet again", player.getName(), player.getID())
    else:
        print('See You Again!')
        player = 'quit'
    return player

########################################
#                                      #
#             MAIN                     #
#                                      #
########################################
def Player():
    player = intro_menu()
    return player

Player()
