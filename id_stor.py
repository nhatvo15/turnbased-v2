import random

def readme():
    print("""Makepool will create a pool randomly in range of n
                 from 9999 to 100000

             Printpool will display the pool

             CheckID will check if the ID already been use""")

def make_pool():
    for i in range(20):
        var = random.randint(9999, 100000)
        print(var)
        file_obj = open('id.txt', 'a')
        file_obj.write(str(var)+' ')
    file_obj.close()

def make_txt():
    _file = open('id.txt', 'a')
    _file.close()

def readfile():
    num = 57291
    my_file = open('id.txt', 'r')
    print(my_file.readlines())
    my_file.close()

def makeID():
    _id = random.randint(9999, 100000)
    return _id

def saveID(_id):
    _file = open('id.txt', 'a')
    _file.write(str(_id)+' ')
    _file.close()

def checkID(val):
    data = open('id.txt', 'r')
    for line in data:
        words = line.split()
    temp = 0
    for item in words:
        if item == str(val):
            temp=1
    print(temp)
        
    data.close()

def IdPC():
    while True:
        print('Welcome to ID Pool Control IdPC: ')
        selection = input('(R)eadme, (M)akepool(Readme_first), (P)rintpool, (C)heckID, (E)xit = ')
        if selection == 'M' or selection =='m':
            make_pool()
            print('\n')
        elif selection == 'P' or selection=='p':
            readfile()
            print('\n')
        elif selection=='R':
            readme()
            print('\n')
        elif selection=='C':
            val = input('Enter ID here: ')
            checkID(val)
            print('\n')
        else:
            print('Bye')
            break

IdPC()

