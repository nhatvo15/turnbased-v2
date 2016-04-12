from Worlds import *

def create_small():
    ws = World_small("Tinee", 2)
    ws.getStat()

def create_medium():
    wm = World_medium("Maria",1)
    wm.getStat()

def create_big():
    wb = World_big("Bee", 4)
    wb.getStat()

def main():
    choice = 0
    while choice!=3:
        print("==============================================")
        choice = eval(input("small=0 medium=1 big=2 := "))
        if choice==0:
            try: create_small()
            except TypeError:
                continue
            
        elif choice==1:
            try: create_medium()
            except TypeError:
                continue
            
        elif choice==2:
            try: create_big()
            except TypeError:
                continue
        print()

main()
