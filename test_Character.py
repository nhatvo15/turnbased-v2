from Character import *
import pickle
#########################################
#ULTILITY functions                     #
#---sub functions support MENU function #
#########################################
def save_character(character):
    with open(character.getName()+'.dat', 'wb') as output:
        pickle.dump(character, output, pickle.HIGHEST_PROTOCOL)
    print('SAVE COMPLETED!!!')

def create_character():
    name = input("Enter character name:")
    character = Character(name)
    save_character(character) #->save immediately
    return character

def load_character(charname):
    try:
        with open(charname+'.dat', 'rb') as input:
            character = pickle.load(input)
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
        print("We meet again", player.getName())
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
    """
    character = intro_menu()
    fight()"""
    load_character('qwe')

    

main()
