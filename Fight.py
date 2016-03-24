import random

opt_list = ['bag','scissor','hammer','bag','scissor']
pl1 = 3
pl2 = 1
if pl1 == pl2:
    print 'tied'
elif opt_list[pl1+1]==opt_list[pl2]:
    print 'pl2 won | ' + opt_list[pl1] + ' < ' + opt_list[pl2]
else:
    print 'pl1 won | ' + opt_list[pl1] + ' > ' + opt_list[pl2]
