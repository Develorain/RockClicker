import pygame
import constants
import os.path

from os import path
from button import Button
from text import Text
from state import State
from mainscreen import MainScreen
from gamescreen import GameScreen
from shopscreen import ShopScreen
from gameoverscreen import GameOverScreen
from profile import Profile

def readProfileDataFromFiles():
    f = open(constants.PRIMARY_FILE_NAME, "r")
    content = f.read()
    array = content.split()
    gemCount1 = int(array[0])
    incrementCount1 = int(array[1])
    passiveCount1 = int(array[2])
    healthCount1 = float(array[3])
    f.close()
    
    f2 = open(constants.SECONDARY_FILE_NAME, "r")
    content2 = f2.read()
    array2 = content2.split()
    gemCount2 = int(array2[0])
    incrementCount2 = int(array2[1])
    passiveCount2 = int(array2[2])
    healthCount2 = float(array2[3])
    f2.close()

    return gemCount1, incrementCount1, passiveCount1, healthCount1, gemCount2, incrementCount2, passiveCount2, healthCount2

def main():
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Rock Clicker")
    display = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    gemCount1, incrementCount1, passiveCount1, healthCount1, gemCount2, incrementCount2, passiveCount2, healthCount2 = readProfileDataFromFiles()

    profile1 = Profile(gemCount1, incrementCount1, passiveCount1, healthCount1)
    profile2 = Profile(gemCount2, incrementCount2, passiveCount2, healthCount2)

    # Create screens
    mainScreen = MainScreen(display, profile1, profile2)

    gameScreen1 = GameScreen(display, profile1, 0, 0)
    shopScreen1 = ShopScreen(display, profile1, 0, 0)
    gameOverScreen1 = GameOverScreen(display, profile1, 0, 0)
    
    gameScreen2 = GameScreen(display, profile2, constants.SCREEN_WIDTH, 0)
    shopScreen2 = ShopScreen(display, profile2, constants.SCREEN_WIDTH, 0)
    gameOverScreen2 = GameOverScreen(display, profile2, constants.SCREEN_WIDTH, 0)

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
                elif profile1.state == State.GAME_OVER_SCREEN:
                    gameOverScreen1.checkForComponentClicks()

                if constants.MULTIPLAYER == True:
                    if profile2.state == State.GAME_SCREEN:
                        gameScreen2.checkForComponentClicks()
                    elif profile2.state == State.SHOP_SCREEN:
                        shopScreen2.checkForComponentClicks()
                    elif profile2.state == State.GAME_OVER_SCREEN:
                        gameOverScreen2.checkForComponentClicks()

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
        elif profile1.state == State.GAME_OVER_SCREEN:
            gameOverScreen1.update()
            gameOverScreen1.draw()
        
        if constants.MULTIPLAYER == True:
            if profile2.state == State.GAME_SCREEN:
                gameScreen2.update(deltaTime)
                gameScreen2.draw()
            elif profile2.state == State.SHOP_SCREEN:
                shopScreen2.update(deltaTime)
                shopScreen2.draw()
            elif profile2.state == State.GAME_OVER_SCREEN:
                gameOverScreen2.update()
                gameOverScreen2.draw()

        pygame.display.update()

if __name__ == '__main__':
    main()