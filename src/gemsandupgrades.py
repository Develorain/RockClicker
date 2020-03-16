

class GemsAndUpgrades():
    INCREMENT_AMOUNT = 1
    
    def __init__(self):
        self.gemCount = 0

    def incrementGems(self):
        self.gemCount = self.gemCount + self.INCREMENT_AMOUNT
    
    def upgrade(self):
        self.INCREMENT_AMOUNT = self.INCREMENT_AMOUNT + 5
        print("Upgraded to " + str(self.INCREMENT_AMOUNT) + " per click")
    
    def getGemCount(self):
        return self.gemCount
