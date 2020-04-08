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
        self.rock = Rock(self.x + constants.CENTER_SCREEN_X, constants.CENTER_SCREEN_Y, 100, 100)

        # Buttons
        self.saveButton = Button("Save", self.x + 700, 0, 100, 50)
        self.shopButton = Button("Shop", self.x + 700, 550, 100, 50)

        # Labels and Dynamic text
        self.gemText = Text("Gem:", self.x + 10, 550, constants.WHITE, "Arial", 25)
        self.gemAmountText = Text(str(self.profile.getGemCount()), self.x + 72, 550, constants.WHITE, "Arial", 25)

        # Rocks
        #self.rock2 = Rock(constants.CENTER_SCREEN_X+constants.SCREEN_WIDTH, constants.CENTER_SCREEN_Y, 100, 100)

        # Buttons
        #self.saveButton2 = Button("Save", 700+constants.SCREEN_WIDTH, 0, 100, 50)
        #self.shopButton2 = Button("Shop", 700+constants.SCREEN_WIDTH, 550, 100, 50)

        # Labels and Dynamic text
        #self.gemText2 = Text("Gem:", 10+constants.SCREEN_WIDTH, 550, constants.WHITE, "Arial", 25)
        #self.gemAmountText2 = Text(str(self.profile.getGemCount()), 72+constants.SCREEN_WIDTH, 550, constants.WHITE, "Arial", 25)

    # Add components to components list
    def attachComponents(self):
        # Rocks
        self.components.append(self.rock)

        # Buttons
        self.components.append(self.saveButton)
        self.components.append(self.shopButton)
        
        # Labels and Dynamic text
        self.components.append(self.gemText)
        self.components.append(self.gemAmountText)

        # Rocks
        #self.components.append(self.rock2)

        # Buttons
        #self.components.append(self.saveButton2)
        #self.components.append(self.shopButton2)
        
        # Labels and Dynamic text
        #self.components.append(self.gemText2)
        #self.components.append(self.gemAmountText2)
    
    # Updates all the components in the screen that change
    def update(self, deltaTime):
        self.profile.handlePassive(deltaTime)

        self.rock.update(deltaTime)
        self.gemAmountText.update(str(self.profile.getGemCount()))

        #if (constants.MULTIPLAYER):
            #self.rock2.update(deltaTime)
            #self.gemAmountText2.update(str(self.profile.getGemCount()))
    
    def checkForComponentClicks(self):
        if self.rock.isBeingClicked() == True:
            self.profile.incrementGems()
        
        if self.saveButton.isBeingClicked() == True:
            f = open(constants.PRIMARY_FILE_NAME, "w")
            f.write(str(self.profile.getGemCount()) + "\n")
            f.write(str(self.profile.getIncrementCount()) + "\n")
            f.write(str(self.profile.getPassiveCount()))
            f.close()
        
        if self.shopButton.isBeingClicked() == True:
            self.profile.state = State.SHOP_SCREEN