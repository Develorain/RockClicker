import pygame
import constants

from rock import Rock
from button import Button
from text import Text
from state import State
from mainscreen import MainScreen
from gamescreen import GameScreen
from shopscreen import ShopScreen
from gemsandupgrades import GemsAndUpgrades

def main():
    global running, display, rock

    # Initialize pygame
    pygame.init()
    display = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Rock Clicker")
    clock = pygame.time.Clock()

    running = True
    state = State.MAIN_SCREEN

    gemsAndUpgrades = GemsAndUpgrades()

    # Create screens
    mainScreen = MainScreen(display)
    gameScreen = GameScreen(display, gemsAndUpgrades)
    shopScreen = ShopScreen(display, gemsAndUpgrades)

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
            shopScreen.update(deltaTime)
            shopScreen.draw()

        pygame.display.update()

if __name__ == '__main__':
    main()

# TODO
# add dying
# add more upgrades
# general refactor required