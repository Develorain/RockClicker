from state import State

class Profile():
    
    def __init__(self):
        # Upgrade 1
        self.INCREMENT_AMOUNT = 1
        self.UPGRADE_INCREMENT_COST = 100
        self.INCREMENT_COUNT = 0

        # Upgrade 2
        self.PASSIVE_AMOUNT = 1
        self.UPGRADE_PASSIVE_COST = 50
        self.PASSIVE_COUNT = 0
        self.PASSIVE_TIMER = 1000  # 1 second per passive tick

        self.gemCount = 100000
        self.passiveTimer = 0

        self.state = State.MAIN_SCREEN
    
    def handlePassive(self, deltaTime):
        self.addToPassiveTimer(deltaTime)

        if (self.isPassiveReady()):
            self.resetPassiveTimer()
            self.passiveIncrementGems()

    def incrementGems(self):
        self.gemCount = self.gemCount + self.INCREMENT_AMOUNT
    
    def passiveIncrementGems(self):
        self.gemCount = self.gemCount + self.PASSIVE_AMOUNT
    
    def upgradeIncrementAmount(self):
        if self.UPGRADE_INCREMENT_COST <= self.gemCount:
            self.INCREMENT_AMOUNT = self.INCREMENT_AMOUNT + 5
            self.gemCount = self.gemCount - self.UPGRADE_INCREMENT_COST
            self.INCREMENT_COUNT = self.INCREMENT_COUNT + 1

            print("New gem count:" + str(self.gemCount))
            print("Upgraded to " + str(self.INCREMENT_AMOUNT) + " per click")
        else:
            print("Can't afford upgrade")
    
    def upgradePassiveIncrementAmount(self):
        if self.UPGRADE_PASSIVE_COST <= self.gemCount:
            self.PASSIVE_AMOUNT = self.PASSIVE_AMOUNT + 1
            self.gemCount = self.gemCount - self.UPGRADE_PASSIVE_COST
            self.PASSIVE_COUNT = self.PASSIVE_COUNT + 1

            print("New gem count:" + str(self.gemCount))
            print("Upgraded to " + str(self.PASSIVE_AMOUNT) + " per second")
        else:
            print("Can't afford upgrade")
    
    def getGemCount(self):
        return self.gemCount
    
    def getIncrementCount(self):
        return self.INCREMENT_COUNT

    def getPassiveCount(self):
        return self.PASSIVE_COUNT

    def isPassiveReady(self):
        if self.passiveTimer >= self.PASSIVE_TIMER:
            return True
        
        return False
    
    def addToPassiveTimer(self, deltaTime):
        self.passiveTimer += deltaTime
    
    def resetPassiveTimer(self):
        self.passiveTimer = 0