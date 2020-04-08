import constants

from state import State
from text import Text
from screen import Screen
from button import Button

class GameOverScreen(Screen):
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
        # Labels and Dynamic text
        self.gameOverText = Text("GAME OVER", self.x + 260, 100, constants.RED, "Arial", 50)

        self.finalGemLabel = Text("FINAL GEM COUNT", self.x + 230, 200, constants.RED, "Arial", 40)
        self.finalGemText = Text(str(self.profile.getGemCount()), self.x + 360, 260, constants.WHITE, "Arial", 40)

        # Buttons
        self.quitButton = Button("Quit", self.x + 370, 360, 100, 50)

    # Add components to components list
    def attachComponents(self):
        # Labels and Dynamic text
        self.components.append(self.gameOverText)
        
        self.components.append(self.finalGemLabel)
        self.components.append(self.finalGemText)

        self.components.append(self.quitButton)
    
    def update(self):
        self.finalGemText.update(str(self.profile.getGemCount()))

    def checkForComponentClicks(self):
        # Determine which save file will be overwritten based on which quit button is being pressed
        if self.quitButton.x < constants.SCREEN_WIDTH:
            f = open(constants.PRIMARY_FILE_NAME, "w")
            print("left quit: ")
            print(self.quitButton.x)
        
        if (self.quitButton.x > constants.SCREEN_WIDTH):
            f = open(constants.SECONDARY_FILE_NAME, "w")
            print("right quit")
        
        # Set the save file to default values, as the character is now dead!
        f.write(str(200) + " ")
        f.write(str(0) + " ")
        f.write(str(0) + " ")
        f.write(str(10) + " ")
        f.close()
        
        print("Game should close now!")
        raise SystemExit