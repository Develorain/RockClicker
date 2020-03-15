from button import Button
from screen import Screen

class MainScreen(Screen):
    def __init__(self, display):
        Screen.__init__(self, display)

        # Create the componenets of the main screen
        self.startButton = Button("Start", 350, 275, 100, 50)

        # Add components to components list
        self.components.append(self.startButton)
    
    def checkForComponentClicks(self, state):
        state = self.startButton.isBeingClicked(state)

        return state