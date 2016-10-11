import pygame
import time


pygame.init()
n=20
step = round(800 / n)
white = (225, 225, 225)
bright = (255, 255, 255)
black = (0, 0, 0)

display_width = 800
display_height = 800

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(white)

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def grid(n, step):
    gameDisplay.fill(white)
    for i in range(0,n):
        pygame.draw.line(gameDisplay, black, (step * i,0),(step * i,800),1)
    for i in range(0,n):
        pygame.draw.line(gameDisplay, black, (0, step * i), (800 , step * i), 1)


def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Welcome to Ranju!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        print mouse
        pygame.display.update()
        clock.tick(15)

def game_loop():

    while True:
        for event in pygame.event.get():
            grid(n, step)
            mouse = pygame.mouse.get_pos()
            print mouse
            for i in range(0,n):
                for j in range(0,n):
                    if step * i < mouse[0] < step * (i+1) and step * j < mouse[1] < step * (j + 1):
                        pygame.draw.rect(gameDisplay, bright, ((step * i)+1,(step * j)+1,step-1, step-1))

            pygame.display.update()
            clock.tick(60)



            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
#intro()
game_loop()
