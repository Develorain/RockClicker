import pygame
import constants

from rock import Rock
from button import Button
from text import Text
from states import State

def main():
    global running, screen, rock

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("RockClicker")
    running = True

    rock = Rock(constants.CENTER_SCREEN_X, constants.CENTER_SCREEN_Y, 100, 100)
    startButton = Button("Start", 350, 275, 100, 50)
    shopButton = Button("Shop", 700, 550, 100, 50)
    gemText = Text("Gems: " + rock.getGemCountAsString(), 10, 550, constants.WHITE, "Arial", 30)

    upgradeButton1 = Button("Upgrade 1", 350, 125, 100, 50)
    upgradeButton2 = Button("Upgrade 2", 350, 200, 100, 50)
    upgradeButton3 = Button("Upgrade 3", 350, 275, 100, 50)
    upgradeButton4 = Button("Upgrade 4", 350, 350, 100, 50)

    state = State.MAIN_SCREEN

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == State.MAIN_SCREEN:
                    state = startButton.isBeingClicked(state)
                
                if state == State.GAME_SCREEN:
                    rock.isBeingClicked()
                    state = shopButton.isBeingClicked(state)
                
                if state == State.SHOP_SCREEN:
                    upgradeButton1.isBeingClicked(state)
                    upgradeButton2.isBeingClicked(state)
                    upgradeButton3.isBeingClicked(state)
                    upgradeButton4.isBeingClicked(state)


            if event.type == pygame.QUIT:
                running = False
        
        # Clears screen
        screen.fill(constants.BLACK)
        
        if state == State.MAIN_SCREEN:
            drawMainScreen(startButton)
        elif state == State.GAME_SCREEN:
            drawGameScreen(rock, gemText, shopButton)
        elif state == State.SHOP_SCREEN:
            drawShopScreen(upgradeButton1, upgradeButton2, upgradeButton3, upgradeButton4)

        pygame.display.update()

def drawMainScreen(startButton):
    startButton.draw(screen)

def drawGameScreen(rock, gemText, shopButton):
    screen.fill(constants.BLACK)
    rock.draw(screen)
    gemText.drawDynamic(screen, "Gems: " + rock.getGemCountAsString())
    shopButton.draw(screen)

def drawShopScreen(upgradeButton1, upgradeButton2, upgradeButton3, upgradeButton4):
    upgradeButton1.draw(screen)
    upgradeButton2.draw(screen)
    upgradeButton3.draw(screen)
    upgradeButton4.draw(screen)

if __name__ == '__main__':
    main()