from Player import *
from World import *
from SAVELOAD import *

SL = SL()

########################
#                      #
#        Menus         #
#                      #
########################
"""
Shop: handle transaction
restockable
"""
def shop():
    pass

"""
Stat: information of the player
toggle-able
"""
def stat():
    pass

"""
Inventory: carry item, equiped items, gold
toggle-able
"""
def inventory():
    pass

"""
Play:

have: size, coordinate, obstackle, bots, boss, npc, secret shop
does: traverse, fight bots, fights boss
loot: exp, gold, dropped-items, secret key
"""
def play():
    pass

########################
#                      #
#        Fight         #
#                      #
########################
def fight(p1, p2):
    opt_list = ['rock', 'scissor', 'paper']
    result = 0
    if p1==p2:
        print('tie ' + opt_list[p1] + ' = ' + opt_list[p2])
    elif p2==(p1+1)%3:
        print('p1 won ' + opt_list[p1] + ' > ' + opt_list[p2])
        result=1
    else:
        print('p2 won ' + opt_list[p1] + ' > ' + opt_list[p2])
        result=2
    return result

def main():
    p1 = Player()
    p2 = Player()
    x = p1.random_choice()
    y = p2.random_choice()
    
    print(p1.getName(), x, p2.getName(), y)

    res = fight(x, y)
    

    
def testFight():
    #get player1, choice1
    p1 = Player()
    x = p1.random_choice()

    #get player2, choice2
    p2 = Player()
    y = p1.random_choice()
    
    print(p1.getName(), x, p2.getName(), y)

    #make p1, p2 fight
    res = fight(x, y)

def testEXP():
    player = Player()
    print(player.getLevel(), player.getExp())
    player.gainExp(700)
    print(player.getLevel(), player.getExp())
    SL.save_character(player)

testFight()


    
