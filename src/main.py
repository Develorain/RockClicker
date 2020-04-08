import pygame
import constants

from button import Button
from text import Text
from state import State
from mainscreen import MainScreen
from gamescreen import GameScreen
from shopscreen import ShopScreen
from profile import Profile

def main():
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Rock Clicker")
    display = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    profile1 = Profile()
    profile2 = Profile()

    # Create screens
    mainScreen = MainScreen(display, profile1, profile2)

    gameScreen1 = GameScreen(display, profile1, 0, 0)
    shopScreen1 = ShopScreen(display, profile1, 0, 0)
    
    gameScreen2 = GameScreen(display, profile2, constants.SCREEN_WIDTH, 0)
    shopScreen2 = ShopScreen(display, profile2, constants.SCREEN_WIDTH, 0)

    # Game loop
    while running:
        deltaTime = clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if profile1.state == State.MAIN_SCREEN:
                    mainScreen.checkForComponentClicks()
                elif profile1.state == State.GAME_SCREEN:
                    gameScreen1.checkForComponentClicks()
                elif profile1.state == State.SHOP_SCREEN:
                    shopScreen1.checkForComponentClicks()

                if profile2.state == State.GAME_SCREEN:
                    gameScreen2.checkForComponentClicks()
                elif profile2.state == State.SHOP_SCREEN:
                    shopScreen2.checkForComponentClicks()

            if event.type == pygame.QUIT:
                running = False
        
        # Clears display
        display.fill(constants.BLACK)
        
        if profile1.state == State.MAIN_SCREEN:
            mainScreen.draw()
        elif profile1.state == State.GAME_SCREEN:
            gameScreen1.update(deltaTime)
            gameScreen1.draw()
        elif profile1.state == State.SHOP_SCREEN:
            shopScreen1.update(deltaTime)
            shopScreen1.draw()
        
        if profile2.state == State.GAME_SCREEN:
            gameScreen2.update(deltaTime)
            gameScreen2.draw()
        elif profile2.state == State.SHOP_SCREEN:
            shopScreen2.update(deltaTime)
            shopScreen2.draw()

        pygame.display.update()
        #print("State1: " + str(profile1.state))
        #print("State2: " + str(profile2.state))

if __name__ == '__main__':
    main()