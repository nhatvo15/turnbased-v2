import random

def readme():
    print("""Makepool will create a pool randomly in range of n
                 from 99 to 200

             Printpool will display the pool

             CheckID will check if the ID already been use""")

def make_pool():
    for i in range(1):
        var = makeID()
        print(var)
        file_obj = open('id.txt', 'w')
        file_obj.write(str(var)+' ')
    file_obj.close()

def make_txt():
    _file = open('id.txt', 'a')
    _file.close()

def readfile():
    my_file = open('id.txt', 'r')
    print(my_file.readlines())
    my_file.close()

def makeID():
    _id = random.randint(99, 200)
    return _id

def saveID(_id):
    _file = open('id.txt', 'a')
    _file.write(str(_id)+' ')
    _file.close()

def checkID(val):
    data = open('id.txt', 'r')
    for line in data:
        words = line.split()
    result = 0
    for item in words:
        if item == str(val):
            result=1        
    data.close()
    print(result)
    return result

def newID_validate():
    check = 1
    while check==1:
        userID = makeID()
        check = checkID(userID)
    return userID

def simulator(times):
    temp = 0
    for i in range(times):
        userID = makeID()
        print("....check ID =", userID)
        check = checkID(userID)
        if check == 0:
            print("AVALABLE")
        else:
            temp = temp + 1
            print("been USED")
    print(temp, 'times random a used ID')

def simulator_write(times):
    for i in range(times):
        userID = makeID()
        print("....check ID =", userID)
        check = checkID(userID)
        if check == 0:
            print("AVALABLE - saving ....")
            saveID(userID)
        else:
            print("been USED")

def IdPC():
    while True:
        print('Welcome to ID Pool Control IdPC: ')
        selection = input('(R)eadme, (M)akepool(Readme_first), (P)rintpool, (C)heckID, (S)imulator, (SR)imulatorWrite, (E)xit = ')
        if selection == 'M' or selection =='m':
            make_pool()
            print('\n')
        elif selection == 'P' or selection=='p':
            readfile()
            print('\n')
        elif selection=='R' or selection=='r':
            readme()
            print('\n')
        elif selection=='C' or selection=='c':
            val = input('Enter ID here: ')
            checkID(val)
            print('\n')
        elif selection=='S' or selection=='s':
            n = eval(input('loops: '))
            simulator(n)
            print('\n')
        elif selection=='SR' or selection=='sr':
            n = eval(input('loops: '))
            simulator_write(n)
            print('\n')
        else:
            print('Bye')
            break
def test():
    userID = newID_validate()
    print(userID)

IdPC()

    

