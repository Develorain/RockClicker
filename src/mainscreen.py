from button import Button

class MainScreen():
    def __init__(self, display):
        self.display = display

        # All the components of the screen
        self.startButton = Button("Start", 350, 275, 100, 50)

        self.components = []
        self.components.append(self.startButton)

    def draw(self):
        for component in self.components:
            component.draw(self.display)
    
    def checkForClicks(self, state):
        state = self.startButton.isBeingClicked(state)

        return state