import constants

from button import Button
from text import Text
from screen import Screen
from state import State

class ShopScreen(Screen):
    def __init__(self, display, profile, x, y):
        Screen.__init__(self, display)
        
        # Give screen access to gems and upgrades
        self.profile = profile

        self.x = x
        self.y = y

        self.initComponents()
        self.attachComponents()
    
    # Create the components of the main screen
    def initComponents(self):
        # Buttons
        self.upgradeButton1 = Button("Increment Amount (Cost " + str(self.profile.incrementUpgradeCost) + ") (+" + str(self.profile.incrementIncreasePerUpgrade) + ")", self.x + 150, 150, 500, 50)
        self.upgradeButton2 = Button("Passive Increment Amount (Cost " + str(self.profile.passiveUpgradeCost) + ") (+" + str(self.profile.passiveIncreasePerUpgrade) + ")", self.x + 150, 225, 500, 50)
        self.backButton = Button("Back", self.x +700, 550, 100, 50)

        # Labels and Dynamic text
        self.availableUpgradesText = Text("Available Upgrades", self.x + constants.CENTER_SCREEN_X-100, 100, constants.WHITE, "Arial", 30)
        self.currentUpgradesText = Text("Current Upgrades", self.x + constants.CENTER_SCREEN_X-100, 325, constants.WHITE, "Arial", 30)

        self.upgrade1Label = Text("Increment Level:", self.x + 200, 375, constants.WHITE, "Arial", 25)
        self.upgrade1Text = Text(str(self.profile.getIncrementCount()) + " (+" + str(self.profile.incrementAmount) + "per click)", self.x + 388, 375, constants.WHITE, "Arial", 25)

        self.upgrade2Label = Text("Passive Increment Level:", self.x + 200, 425, constants.WHITE, "Arial", 25)
        self.upgrade2Text = Text(str(self.profile.getPassiveCount()), self.x + 485, 425, constants.WHITE, "Arial", 25)

        self.gemLabel = Text("Gem:", self.x + 10, 550, constants.WHITE, "Arial", 25)
        self.gemText = Text(str(self.profile.getGemCount()), self.x + 72, 550, constants.WHITE, "Arial", 25)

        self.healthLabel = Text("Health:", self.x + 340, 550, constants.WHITE, "Arial", 25)
        self.healthText = Text(str(self.profile.health), self.x + 422, 550, constants.WHITE, "Arial", 25)
    
    # Add components to components list
    def attachComponents(self):
        # Buttons
        self.components.append(self.upgradeButton1)
        self.components.append(self.upgradeButton2)
        self.components.append(self.backButton)

        # Labels and dynamic text
        self.components.append(self.availableUpgradesText)
        self.components.append(self.currentUpgradesText)
        self.components.append(self.upgrade1Label)
        self.components.append(self.upgrade1Text)
        self.components.append(self.upgrade2Label)
        self.components.append(self.upgrade2Text)
        self.components.append(self.gemLabel)
        self.components.append(self.gemText)
        self.components.append(self.healthLabel)
        self.components.append(self.healthText)

    def update(self, deltaTime):
        #self.profile.handlePassive(deltaTime)

        self.gemText.update(str(self.profile.getGemCount()))
        self.healthText.update(str(self.profile.health))
        self.upgrade1Text.update(str(self.profile.getIncrementCount()) + " (+" + str(self.profile.incrementAmount) + " per click)")
        self.upgrade2Text.update(str(self.profile.getPassiveCount()) + " (+" + str(self.profile.passiveAmount) + " per second)")
    
    def checkForComponentClicks(self):
        if self.upgradeButton1.isBeingClicked() == True:
            self.profile.upgradeIncrementAmount()
        elif self.upgradeButton2.isBeingClicked() == True:
            self.profile.upgradePassiveIncrementAmount()
        elif self.backButton.isBeingClicked() == True:
            self.profile.state = State.GAME_SCREEN