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
    startButton = Button("Start", 400, 300, 100, 50)
    shopButton = Button("Shop", 700, 550, 100, 50)
    gemText = Text("Gems: " + rock.getGemCountAsString(), 10, 550, constants.WHITE, "Arial", 30)

    state = State.MAIN_MENU

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                rock.isBeingClicked()
                shopButton.isBeingClicked()

                if state == State.MAIN_MENU:
                    state = State.GAME_SCREEN
                else:
                    state = State.MAIN_MENU

            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(constants.BLACK)
        
        if state == State.MAIN_MENU:
            draw1(startButton)
        else:
            draw2(rock, gemText, shopButton)

        pygame.display.update()

def draw1(startButton):
    startButton.draw(screen)

def draw2(rock, gemText, shopButton):
    screen.fill(constants.BLACK)
    rock.draw(screen)
    gemText.drawDynamic(screen, "Gems: " + rock.getGemCountAsString())
    shopButton.draw(screen)

if __name__ == '__main__':
    main()