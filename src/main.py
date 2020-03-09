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
        drawGemCount(screen)
        pygame.display.update()

def drawRock():
    pygame.draw.circle(screen, white, centerOfScreen, radius)

def drawGemCount(screen):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render(str(gemCount), True, white, None)
    screen.blit(text, (0, 550))

if __name__ == '__main__':
    main()