import random
import pickle
import os.path
from Item_Class import *
from SAVELOAD import *

SL = SL()
"""ID maker"""
def makeID():
    _id = random.randint(0, 200)
    return _id

def checkID(val):
    data = open('id_item.txt', 'r')
    for line in data:
        words = line.split()
    temp = 0
    for item in words:
        if item == str(val):
            temp=1        
    data.close()
    return temp

def saveID(val):
    data = open('id_item.txt', 'a')
    data.write(str(val)+' ')
    data.close

def newID_validate():
    check = 1
    while check==1:
        userID = makeID()
        check = checkID(userID)
    return userID

def main():
    #create Wooden Hammer Level 3
    weapon = Weapon()
    weapon.setType('Hammer')
    weapon.setName('Wooden Hammer')
    weapon.setLevel(3)
    weapon._repr()
    SL.save_item(weapon)

main()
    
