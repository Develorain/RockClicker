import pygame
import constants

from rock import Rock

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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                rock.isBeingClicked()

            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(constants.BLACK)

        drawRock()
        drawGemCount()
        drawShopButton()
        pygame.display.update()

def drawRock():
    pygame.draw.rect(screen, constants.WHITE, (constants.CENTER_SCREEN_X - (rockWidth / 2), constants.CENTER_SCREEN_Y - (rockHeight / 2), rockWidth, rockHeight))

def drawGemCount():
    counter = rock.getGemCount()

    font = pygame.font.SysFont('Arial', 30)
    text = font.render("Gems: " + str(counter), True, constants.WHITE, None)
    screen.blit(text, (10, 550))

def drawShopButton():
    pygame.draw.rect(screen, constants.WHITE, (700, 550, 100, 50))

if __name__ == '__main__':
    main()