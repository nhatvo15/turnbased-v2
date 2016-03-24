from Character import *
import pickle

        
def main():
    with open('savegame.pkl', 'rb') as input:
        player = pickle.load(input)

    print player.getName(), player.getSpeed()

main()
