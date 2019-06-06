import pygame
import os

player1 = True
player2 = False

def line(coords1, coords2):
    if player1:
        pygame.draw.line(screen, (0,127,255), (coords1), (coords2), 4)
    if player2:
        pygame.draw.line(screen, (255,69,0), (coords1), (coords2), 4)

pygame.init()
screen = screen = pygame.display.set_mode((800,600))
play_background = pygame.image.load(os.path.join("images", "playbackground.png"))

running = True

circle1_selected = False
circle2_selected = False

while running:
    screen.blit(play_background, (0,0))

    circle1 = pygame.draw.circle(screen, (0,127,255), (200, 200), 6, 0)
    circle2 = pygame.draw.circle(screen, (0,127,255), (300, 300), 6, 0)

    pygame.draw.circle(screen, (255,69,0), (450, 250), 6, 0)

    for event in pygame.event.get():
        if circle1_selected:
            pygame.draw.circle(screen, (248,248,255), (200, 200), 8, 3)
        if circle2_selected:
            pygame.draw.circle(screen, (248,248,255), (300, 300), 8, 3)

        if event.type == pygame.QUIT:
            running = False
        if player1:
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(195,211)) and (y in range(195,211)):
                    pygame.draw.circle(screen, (248,248,255), (200, 200), 7, 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if circle1.collidepoint(x, y):
                    circle1_selected = not circle1_selected
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(295,311)) and (y in range(295,311)):
                    pygame.draw.circle(screen, (248,248,255), (300, 300), 7, 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if circle2.collidepoint(x, y):
                    circle2_selected = not circle2_selected


        pygame.display.flip()
