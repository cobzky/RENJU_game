import pygame
import time


pygame.init()
n=20
step = round(800 / n)
white = (225, 225, 225)
bright = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((800,800))
gameDisplay.fill(white)

def grid(n, step):
    gameDisplay.fill(white)
    for i in range(0,n):
        pygame.draw.line(gameDisplay, black, (step * i,0),(step * i,800),1)
    for i in range(0,n):
        pygame.draw.line(gameDisplay, black, (0, step * i), (800 , step * i), 1)
grid(n, step)


while True:
    for event in pygame.event.get():
        grid(n, step)
        mouse = pygame.mouse.get_pos()
        print mouse
        for i in range(0,n):
            for j in range(0,n):
                if step * i < mouse[0] < step * (i+1) and step * j < mouse[1] < step * (j + 1):
                    pygame.draw.rect(gameDisplay, bright, ((step * i)+1,(step * j)+1,step-2, step-2))

        pygame.display.update()
        clock.tick(60)



        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
