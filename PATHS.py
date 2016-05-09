import os.path

class PATH(object):
    def __init__(self):
        self._PATH = '/home/nvo001/files/csc446/turnbased-v2/savegames/'

    def getPATH(self):
        return self._PATH
        
    def world(self, worldname):
        return os.path.join(self._PATH, worldname+".world")

    def character(self, charname):
        return os.path.join(self._PATH, charname+".character")

    def item(self, itemname):
        return os.path.join(self._PATH, itemname+".item")
    
    def getCharacters(self):
        for file in self.full_file_paths:
            if file.endswith(".character"):
                print(f)

    def getWorlds(self):
        for file in self.full_file_paths:
            if file.endswith(".world"):
                print(f)
    
    def README(self):
        print("""change the self._PATH to match your machine if you
              execute this game on your gig""")
                            

