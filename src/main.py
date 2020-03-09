import pygame

width = 800
height = 600
radius = 100
white = (255, 255, 255)
black = (0, 0, 0)
centerOfScreen = (400, 300)

def main():
    global running, screen, gemCount

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RockClicker")
    running = True
    gemCount = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                gemCount = gemCount + 1
                print(gemCount)

            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(black)

        drawRock()
        drawGemCount()
        pygame.display.update()

def drawRock():
    pygame.draw.circle(screen, white, centerOfScreen, radius)

def drawGemCount():
    font = pygame.font.SysFont('Arial', 30)
    text = font.render("Gems: " + str(gemCount), True, white, None)
    screen.blit(text, (10, 550))

if __name__ == '__main__':
    main()