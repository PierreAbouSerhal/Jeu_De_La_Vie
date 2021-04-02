class Cell:

    def __init__(self):
        self.isAlive  = False
        self.clickCnt = 0
        self.nbrs     = 0
    
    def die(self):
        self.isAlive = False

    def live(self):
        self.isAlive = True  