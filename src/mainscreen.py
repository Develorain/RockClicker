from button import Button
from screen import Screen
from state import State

class MainScreen(Screen):
    def __init__(self, display):
        Screen.__init__(self, display)

        self.init()
    
    def init(self):
        # Create the components of the main screen
        self.startButton = Button("Start", 350, 225, 100, 50)
        self.quitButton = Button("Quit", 350, 300, 100, 50)

        # Add components to components list
        self.components.append(self.startButton)
        self.components.append(self.quitButton)
    
    def checkForComponentClicks(self, state):
        if self.startButton.isBeingClicked(state) == True:
            state = State.GAME_SCREEN
        
        if self.quitButton.isBeingClicked(state) == True:
            print("Game should close now!")
            raise SystemExit

        return state