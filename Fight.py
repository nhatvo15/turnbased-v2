import random
def fightv1():
    opt_list = ['bag','scissor','hammer','bag','scissor']
    pl1 = 1
    pl2 = 2
    if pl1 == pl2:
        print('tied')
    elif opt_list[pl1+1]==opt_list[pl2]:
        print('pl2 won | ' + opt_list[pl1] + ' < ' + opt_list[pl2])
    else:
        print('pl1 won | ' + opt_list[pl1] + ' > ' + opt_list[pl2])

def fightv2():
    opt_list = ['rock', 'scissor', 'paper']
    x = 2
    y = 0

    if x==y:
        print('tie ' + opt_list[x] + ' = ' + opt_list[y])
    elif y==(x+1)%3:
        print('p1 won ' + opt_list[x] + ' > ' + opt_list[y])
    else:
        print('p2 won ' + opt_list[y] + ' > ' + opt_list[x])

fightv2()
