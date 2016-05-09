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
        itemID = makeID()
        check = checkID(itemID)
    return itemID
    

def main():
    #create Wooden Hammer Level 3
    weapon = Weapon()
    weapon.setType('Hammer')
    weapon.setName('Wooden Hammer')
    weapon.setLevel(3)
    _ID = newID_validate()
    weapon.setID(_ID)
    weapon._repr()
    SL.save_item(weapon)

    #create mana potion
    manaPotion = Potion(1)
    _ID = newID_validate()
    manaPotion.setID(_ID)
    manaPotion._repr()
    SL.save_item(manaPotion)

    """
    #create consumable potion
    shieldboost = Consumable()
    shieldboost.setType(4)
    shieldboost.setBuff(10)
    _ID = newID_validate()
    shieldboost.setID(_ID)
    shieldboost._repr()
    SL.save_item(shieldboost)
    """

def testConsumable():
    sb = Consumable()
    sb.setType(4)
    sb.setBuff(10)
    _ID = newID_validate()
    sb.setID(_ID)
    sb._repr()

main()
    
