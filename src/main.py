import pygame
import constants

from rock import Rock
from button import Button
from text import Text
from states import State
from mainscreen import MainScreen
from gamescreen import GameScreen
from shopscreen import ShopScreen

def main():
    global running, display, rock

    # Initialize pygame
    pygame.init()
    display = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Rock Clicker")
    clock = pygame.time.Clock()

    running = True
    state = State.MAIN_SCREEN

    # Create screens
    mainScreen = MainScreen(display)
    gameScreen = GameScreen(display)
    shopScreen = ShopScreen(display)

    # Game loop
    while running:
        deltaTime = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == State.MAIN_SCREEN:
                    state = mainScreen.checkForComponentClicks(state)
                elif state == State.GAME_SCREEN:
                    state = gameScreen.checkForComponentClicks(state)
                elif state == State.SHOP_SCREEN:
                    state = shopScreen.checkForComponentClicks(state)

            if event.type == pygame.QUIT:
                running = False
        
        # Clears display
        display.fill(constants.BLACK)
        
        if state == State.MAIN_SCREEN:
            mainScreen.draw()
        elif state == State.GAME_SCREEN:
            gameScreen.update(deltaTime)
            gameScreen.draw()
        elif state == State.SHOP_SCREEN:
            shopScreen.draw()

        pygame.display.update()

if __name__ == '__main__':
    main()