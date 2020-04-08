import constants

from rock import Rock
from button import Button
from text import Text
from screen import Screen
from state import State

class GameScreen(Screen):
    def __init__(self, display, profile, x, y):
        Screen.__init__(self, display)

        # Give screen access to gems and upgrades
        self.profile = profile
        self.x = x
        self.y = y

        self.initComponents()
        self.attachComponents()
    
    # Create the components of the game screen
    def initComponents(self):
        # Rocks
        self.rock = Rock(self.x + constants.CENTER_SCREEN_X, constants.CENTER_SCREEN_Y, self.profile.health * 10 + 50, self.profile.health * 10 + 50, self.profile)

        # Buttons
        self.saveButton = Button("Save", self.x + 700, 0, 100, 50)
        self.shopButton = Button("Shop", self.x + 700, 550, 100, 50)

        # Labels and Dynamic text
        self.gemLabel = Text("Gem:", self.x + 10, 550, constants.WHITE, "Arial", 25)
        self.gemText = Text(str(self.profile.getGemCount()), self.x + 72, 550, constants.WHITE, "Arial", 25)

        self.healthLabel = Text("Health:", self.x + 340, 550, constants.WHITE, "Arial", 25)
        self.healthText = Text(str(self.profile.health), self.x + 422, 550, constants.WHITE, "Arial", 25)

    # Add components to components list
    def attachComponents(self):
        # Rocks
        self.components.append(self.rock)

        # Buttons
        self.components.append(self.saveButton)
        self.components.append(self.shopButton)
        
        # Labels and Dynamic text
        self.components.append(self.gemLabel)
        self.components.append(self.gemText)

        self.components.append(self.healthLabel)
        self.components.append(self.healthText)
    
    # Updates all the components in the screen that change
    def update(self, deltaTime):
        self.profile.handlePassive(deltaTime)

        self.rock.update(deltaTime)
        self.gemText.update(str(self.profile.getGemCount()))
        self.healthText.update(str(self.rock.profile.health))
    
    def checkForComponentClicks(self):
        if self.rock.isBeingClicked() == True:
            self.profile.incrementGems()
        
        if self.saveButton.isBeingClicked() == True:
            # Determine which file will be overwritten based on which save is being pressed
            if self.saveButton.x < constants.SCREEN_WIDTH:
                f = open(constants.PRIMARY_FILE_NAME, "w")
            
            if (self.saveButton.x > constants.SCREEN_WIDTH):
                f = open(constants.SECONDARY_FILE_NAME, "w")
            
            f.write(str(self.profile.getGemCount()) + " ")
            f.write(str(self.profile.getIncrementCount()) + " ")
            f.write(str(self.profile.getPassiveCount()) + " ")
            f.write(str(self.profile.health) + " ")
            f.close()
        
        if self.shopButton.isBeingClicked() == True:
            self.profile.state = State.SHOP_SCREEN