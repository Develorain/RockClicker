import pygame
import constants

from rock import Rock
from button import Button
from text import Text

def main():
    global running, screen, rock

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("RockClicker")
    running = True

    rock = Rock(constants.CENTER_SCREEN_X, constants.CENTER_SCREEN_Y, 100, 100)
    shopButton = Button("Shop", 700, 550, 100, 50)
    gemText = Text("Gems: " + rock.getGemCountAsString(), 10, 550, constants.WHITE, "Arial", 30)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                rock.isBeingClicked()
                shopButton.isBeingClicked()

            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(constants.BLACK)
        rock.draw(screen)
        gemText.drawDynamic(screen, "Gems: " + rock.getGemCountAsString())
        shopButton.draw(screen)
        pygame.display.update()

if __name__ == '__main__':
    main()