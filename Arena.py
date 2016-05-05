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
        print('tie ' + opt_list[p1] + ' = ' + opt_list[p2], end=' ')
    elif p2==(p1+1)%3:
        print('p1 won ' + opt_list[p1] + ' > ' + opt_list[p2], end=' ')
        result=1
    else:
        print('p2 won ' + opt_list[p1] + ' > ' + opt_list[p2], end=' ')
        result=2
    return result

def deathMatch(p1, p2):
    while p1.getHp()>0 and p2.getHp()>0:
        x=p1.random_choice()
        y=p2.random_choice()
        res=fight(x,y)
        print(p1.getHp(), p2.getHp())
        p1_won = (p1.getWeapon(x) - p2.getShield())
        p2_won = (p2.getWeapon(y) - p1.getShield())
        if res==1:
            p2.incHp((-1)*p1_won)
        elif res==2:
            p1.incHp((-1)*p2_won)
        SL.save_character(p1)
        SL.save_character(p2)

    if p1.getHp()==0:
        winner=p2
        p2.gainExp(p1.bounty())
    elif p2.getHp()==0:
        winner=p1
        p1.gainExp(p2.bounty())
    SL.save_character(p1)
    SL.save_character(p2)

def main():
    p1 = Player()
    p2 = Player()
    p1.setExp(90)
    p2.setExp(90)
    deathMatch(p1, p2)
    print(p1._repr())
    print(p2._repr())
    

    
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
    p1_won = (p1.getWeapon(x) - p2.getShield())
    p2_won = (p2.getWeapon(y) - p1.getShield())
    if res==1:
        p2.incHp((-1)*p1_won)
    elif res==2:
        p1.incHp((-1)*p2_won)

    print(p1.getHp(), p2.getHp())
    SL.save_character(p1)
    SL.save_character(p2)
        

def testEXP():
    player = Player()
    print(player.getLevel(), player.getExp())
    player.gainExp(700)
    print(player.getLevel(), player.getExp())
    SL.save_character(player)

main()


    
