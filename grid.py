import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((800,800))
gameDisplay.fill(white)

def grid(n):
    step = round(800 / n)
    for i in range(0,n):
        pygame.draw.line(gameDisplay, black, (step * i,0),(step * i,800),1)
    for i in range(0,n):
        pygame.draw.line(gameDisplay, black, (0, step * i), (800 , step * i), 1)
grid(50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
