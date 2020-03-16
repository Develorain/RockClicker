class GemsAndUpgrades():
    INCREMENT_AMOUNT = 1
    PASSIVE_INCREMENT_AMOUNT = 1
    PASSIVE_INCREMENT_TIMER = 1000  # 1 second per passive tick
    
    def __init__(self):
        self.gemCount = 0
        self.passiveIncrementTimer = 0
    
    def handlePassive(self, deltaTime):
        self.addToPassiveTimer(deltaTime)

        if (self.isPassiveReady()):
            self.resetPassiveIncrementTimer()
            self.passiveIncrementGems()

    def incrementGems(self):
        self.gemCount = self.gemCount + self.INCREMENT_AMOUNT
    
    def passiveIncrementGems(self):
        self.gemCount = self.gemCount + self.PASSIVE_INCREMENT_AMOUNT
    
    def upgradeIncrementAmount(self):
        self.INCREMENT_AMOUNT = self.INCREMENT_AMOUNT + 5
        print("Upgraded to " + str(self.INCREMENT_AMOUNT) + " per click")
    
    def upgradePassiveIncrementAmount(self):
        self.PASSIVE_INCREMENT_AMOUNT = self.PASSIVE_INCREMENT_AMOUNT + 1
        print("Upgraded to " + str(self.PASSIVE_INCREMENT_AMOUNT) + " per second")
    
    def getGemCount(self):
        return self.gemCount

    def isPassiveReady(self):
        if self.passiveIncrementTimer >= self.PASSIVE_INCREMENT_TIMER:
            return True
        
        return False
    
    def addToPassiveTimer(self, deltaTime):
        self.passiveIncrementTimer += deltaTime
    
    def resetPassiveIncrementTimer(self):
        self.passiveIncrementTimer = 0