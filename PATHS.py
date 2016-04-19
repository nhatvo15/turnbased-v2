import os.path

class PATH(object):
    def __init__(self):
        self._PATH = '/home/nvo001/files/csc446/turnbased-v2/savegames/'

    def world(self, worldname):
        return os.path.join(self._PATH, worldname+".world")

    def character(self, charname):
        return os.path.join(self._PATH, charname+".character")

    def README(self):
        print("""change the self._PATH to match your machine if you
              execute this game on your gig""")
                            

