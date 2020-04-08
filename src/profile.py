from state import State

class Profile():
    def __init__(self, gemCount, incrementCount, passiveCount, health):
        self.gemCount = gemCount
        self.health = health

        # Upgrade 1 stats
        self.incrementCount = incrementCount # how many times this has been upgraded
        self.incrementIncreasePerUpgrade = 5 # how much the gem/click goes up by per upgrade
        self.incrementAmount = self.incrementCount * self.incrementIncreasePerUpgrade # how much gems go up per click
        self.incrementUpgradeCost = 100 # cost of upgrade

        # Upgrade 2 stats
        self.passiveCount = passiveCount
        self.passiveIncreasePerUpgrade = 1
        self.passiveAmount = self.passiveCount * self.passiveIncreasePerUpgrade  # how much gems go up per second
        self.passiveUpgradeCost = 50
        self.PASSIVE_TIMER = 1000  # 1 second per passive tick
        self.passiveTimer = 0

        # Profiles are created to start from the main menu
        self.state = State.MAIN_SCREEN
    
    def handlePassive(self, deltaTime):
        self.addToPassiveTimer(deltaTime)

        if (self.isPassiveReady()):
            self.resetPassiveTimer()
            self.passiveIncrementGems()

    def incrementGems(self):
        self.gemCount = self.gemCount + self.incrementAmount
    
    def passiveIncrementGems(self):
        self.gemCount = self.gemCount + self.passiveAmount
    
    def upgradeIncrementAmount(self):
        if self.incrementUpgradeCost <= self.gemCount:
            self.incrementAmount = self.incrementAmount + self.incrementIncreasePerUpgrade
            self.gemCount = self.gemCount - self.incrementUpgradeCost
            self.incrementCount = self.incrementCount + 1

            print("New gem count:" + str(self.gemCount))
            print("Upgraded to " + str(self.incrementAmount) + " per click")
        else:
            print("Can't afford upgrade")
    
    def upgradePassiveIncrementAmount(self):
        if self.passiveUpgradeCost <= self.gemCount:
            self.passiveAmount = self.passiveAmount + self.passiveIncreasePerUpgrade
            self.gemCount = self.gemCount - self.passiveUpgradeCost
            self.passiveCount = self.passiveCount + 1

            print("New gem count:" + str(self.gemCount))
            print("Upgraded to " + str(self.passiveAmount) + " per second")
        else:
            print("Can't afford upgrade")
    
    def getGemCount(self):
        return self.gemCount
    
    def getIncrementCount(self):
        return self.incrementCount

    def getPassiveCount(self):
        return self.passiveCount

    def isPassiveReady(self):
        if self.passiveTimer >= self.PASSIVE_TIMER:
            return True
        
        return False
    
    def addToPassiveTimer(self, deltaTime):
        self.passiveTimer += deltaTime
    
    def resetPassiveTimer(self):
        self.passiveTimer = 0