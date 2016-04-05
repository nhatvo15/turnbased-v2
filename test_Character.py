from Character import *
import pickle
import random
#########################################
#SUPPORT functions                      #
#---sub functions support ULTT function #
#########################################
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
#ULTILITY functions                     #
#---sub functions support MENU function #
#########################################
def save_character(character):
    with open(character.getName()+'.dat', 'wb') as _file: #save by ID instead by name
        pickle.dump(character, _file, pickle.HIGHEST_PROTOCOL)
    print('SAVE COMPLETED!!!')

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
        with open(charname+'.dat', 'rb') as _file: #load by charname.getID instead of getName()
            character = pickle.load(_file)
            print("We meet again", character.getName())
    except FileNotFoundError:
        ask = input('Try again?[y/n]')
        if ask == 'y':
            charname = input("Enter your character name again: ")
            character = load_character(charname)
        else:
            print('LOAD FAIL!')
            character = 'LOAD FAIL!'
    print('LOAD COMPLETED!!!')
    return character

########################################
#MENU functions                        #
#---compile sub functions              #
########################################
def intro_menu():
    print("Welcome to the game!!!")
    opt = input("(N)ew charater/(L)oad character:")
    if opt == "N":
        player = create_character() #->create
        print(player.getName())
        print("Greetings new comer", player.getName())
    elif opt == "L":
        charname = input("Enter your character name: ")
        player = load_character(charname)
    else:
        print('Restart!')
        player = intro_menu()
    return player

def fight():
    print("""
    ->import world
    ->interative with Arena()
    ->save_character() 
    """)


########################################
#MAIN                                  #
########################################
def main():
    player = intro_menu()
    print(player.getID())
    

main()
