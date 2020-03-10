import pygame
import constants

from rock import Rock
from button import Button

# Dimensions
rockWidth = 100
rockHeight = 100

def main():
    global running, screen, rock

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("RockClicker")
    running = True

    rock = Rock(constants.CENTER_SCREEN_X, constants.CENTER_SCREEN_Y, 100, 100)
    shopButton = Button("Shop", 700, 550, 100, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                rock.isBeingClicked()

            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(constants.BLACK)

        rock.draw(screen)
        drawGemCount()
        shopButton.draw(screen)
        pygame.display.update()

def drawGemCount():
    font = pygame.font.SysFont('Arial', 30)
    text = font.render("Gems: " + str(rock.getGemCount()), True, constants.WHITE, None)
    screen.blit(text, (10, 550))
    #pygame.draw.rect(screen, constants.WHITE, )

if __name__ == '__main__':
    main()