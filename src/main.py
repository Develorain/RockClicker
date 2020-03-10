import pygame

# Dimensions
screenWidth = 800
screenHeight = 600
rockWidth = 100
rockHeight = 100

# Colours
white = (255, 255, 255)
black = (0, 0, 0)

# Positions
centerScreenX = screenWidth / 2
centerScreenY = screenHeight / 2

def main():
    global running, screen

    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("RockClicker")
    running = True
    gemCount = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                gemCount = checkIfPlayerClickingOnRock(gemCount)

            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(black)

        drawRock()
        drawGemCount(gemCount)
        drawShopButton()
        pygame.display.update()

def checkIfPlayerClickingOnRock(gemCount):
    mouse = pygame.mouse.get_pos()
    
    if isClickingOnRock(mouse[0], mouse[1]):
        gemCount = gemCount + 1
    
    return gemCount

def isClickingOnRock(x, y):
    if x > centerScreenX - rockWidth / 2 and x < centerScreenX + rockWidth / 2:
        if y > centerScreenY - rockHeight / 2 and y < centerScreenY + rockHeight / 2:
            return True

    return False

def drawRock():
    pygame.draw.rect(screen, white, (centerScreenX - (rockWidth / 2), centerScreenY - (rockHeight / 2), rockWidth, rockHeight))

def drawGemCount(gemCount):
    font = pygame.font.SysFont('Arial', 30)
    text = font.render("Gems: " + str(gemCount), True, white, None)
    screen.blit(text, (10, 550))

def drawShopButton():
    pygame.draw.rect(screen, white, (700, 550, 100, 50))

if __name__ == '__main__':
    main()