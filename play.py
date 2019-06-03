import pygame
import game, random, math
import os

red = (255, 0, 0)
width = 800
height = 600
circle_num = 20
tick = 2
speed = 5

JOSE = True
JOSETTE = False

pygame.init()
screen = screen = pygame.display.set_mode((800,600))
play_background = pygame.image.load(os.path.join("images", "playbackground.png"))
portrait_jose = pygame.image.load(os.path.join("images", "play_jose.png"))
portrait_josette = pygame.image.load(os.path.join("images", "play_josette.png"))
dot = pygame.image.load(os.path.join("images", "dot.png"))
beerdot = pygame.image.load(os.path.join("images", "beerdot.png"))
screen.blit(play_background, (5,5))
if JOSE:
    screen.blit(portrait_jose, [20, 20])
    screen.blit(portrait_josette, [580, 400])
if JOSETTE:
    screen.blit(portrait_josette, [20, 20])
    screen.blit(portrait_jose, [580, 400])

class circle():
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(120, 420)
        self.r = 5

    def new(self):
        screen.blit(dot, (self.x, self.y))
        # pygame.draw.circle(screen, red, (self.x, self.y), self.r, tick)

c = []
for i in range(circle_num):
    c.append('c'+str(i))
    c[i] = circle()
    shouldprint = True
    for j in range(len(c)):
        if i != j:
            dist = int(math.hypot(c[i].x - c[j].x, c[i].y - c[j].y))
            if dist < int(c[i].r*2):
                shouldprint = False
    if shouldprint:
        dot_rect = pygame.draw.rect(screen, (190, 190, 255), [c[i].x, c[i].y, 40, 40])
        c[i].new()
        pygame.display.update()

while True:
    for event in pygame.event.get():
        # if event.type == pygame.MOUSEMOTION:
        #     x, y = event.pos
        #     if dot_rect.collidepoint(c[i].x, c[i].y):
        #         screen.blit(beerdot, [c[i].x, c[i].y])
        #         print("Does it woooork?!!")
        #         pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if dot_rect.collidepoint(c[i].x, c[i].y):
                print("Oh wow it worked?!")
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
