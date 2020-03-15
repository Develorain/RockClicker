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

    pygame.init()
    display = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("RockClicker")
    running = True

    state = State.MAIN_SCREEN

    mainScreen = MainScreen(display)
    gameScreen = GameScreen(display)
    shopScreen = ShopScreen(display)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == State.MAIN_SCREEN:
                    state = mainScreen.checkForClicks(state)
                elif state == State.GAME_SCREEN:
                    #rock.isBeingClicked()
                    #state = shopButton.isBeingClicked(state)

                    state = gameScreen.checkForClicks(state)
                elif state == State.SHOP_SCREEN:
                    state = shopScreen.checkForClicks(state)

                    #upgradeButton1.isBeingClicked(state)
                    #upgradeButton2.isBeingClicked(state)
                    #upgradeButton3.isBeingClicked(state)
                    #upgradeButton4.isBeingClicked(state)


            if event.type == pygame.QUIT:
                running = False
        
        # Clears display
        display.fill(constants.BLACK)
        
        if state == State.MAIN_SCREEN:
            mainScreen.draw()
            #drawMainScreen(startButton)
        elif state == State.GAME_SCREEN:
            gameScreen.draw()
            #drawGameScreen(rock, gemText, shopButton)
        elif state == State.SHOP_SCREEN:
            shopScreen.draw()
            #drawShopScreen(upgradeButton1, upgradeButton2, upgradeButton3, upgradeButton4)

        pygame.display.update()

def drawMainScreen(startButton):
    startButton.draw(display)

def drawGameScreen(rock, gemText, shopButton):
    display.fill(constants.BLACK)
    rock.draw(display)
    gemText.drawDynamic(display, "Gems: " + rock.getGemCountAsString())
    shopButton.draw(display)

def drawShopScreen(upgradeButton1, upgradeButton2, upgradeButton3, upgradeButton4):
    upgradeButton1.draw(display)
    upgradeButton2.draw(display)
    upgradeButton3.draw(display)
    upgradeButton4.draw(display)

if __name__ == '__main__':
    main()