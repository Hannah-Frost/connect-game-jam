import pygame
import os

player1 = True
player2 = False

circle1_selected = False
circle2_selected = False
circle3_selected = False
show_next_button = False

def line(coords1, coords2):
    if player1:
        pygame.draw.line(screen, (0,127,255), (coords1), (coords2), 4)
    if player2:
        pygame.draw.line(screen, (255,69,0), (coords1), (coords2), 4)

pygame.init()
screen = screen = pygame.display.set_mode((800,600))
play_background = pygame.image.load(os.path.join("images", "playbackground.png"))
next_button_image = pygame.image.load(os.path.join("images", "next_button.png"))

running = True

while running:
    screen.blit(play_background, (0,0))

    circle1 = pygame.draw.circle(screen, (0,127,255), (200, 200), 6, 0)
    circle2 = pygame.draw.circle(screen, (0,127,255), (300, 300), 6, 0)
    circle3 = pygame.draw.circle(screen, (0,127,255), (550, 450), 6, 0)

    pygame.draw.circle(screen, (255,69,0), (450, 250), 6, 0)

    for event in pygame.event.get():
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
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(545,511)) and (y in range(445,461)):
                    pygame.draw.circle(screen, (248,248,255), (550, 450), 7, 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if circle3.collidepoint(x, y):
                    circle3_selected = not circle3_selected
            if circle1_selected:
                pygame.draw.circle(screen, (248,248,255), (200, 200), 8, 3)
                selected = 0
                circles = [circle1_selected, circle2_selected, circle3_selected]
                for x in circles:
                    if x == True:
                        selected += 1
                if selected > 2:
                    show_next_button = False
                if selected == 2:
                    show_next_button = True
                else:
                    show_next_button = False
            if circle2_selected:
                pygame.draw.circle(screen, (248,248,255), (300, 300), 8, 3)
                selected = 0
                circles = [circle1_selected, circle2_selected, circle3_selected]
                for x in circles:
                    if x == True:
                        selected += 1
                if selected > 2:
                    show_next_button = False
                if selected == 2:
                    show_next_button = True
                else:
                    show_next_button = False
            if circle3_selected:
                pygame.draw.circle(screen, (248,248,255), (550, 450), 8, 3)
                selected = 0
                circles = [circle1_selected, circle2_selected, circle3_selected]
                for x in circles:
                    if x == True:
                        selected += 1
                if selected > 2:
                    show_next_button = False
                if selected == 2:
                    show_next_button = True
                else:
                    show_next_button = False
        if show_next_button:
            next_button = pygame.draw.rect(screen, (190, 190, 255), [550, 105, 120, 30])
            screen.blit(next_button_image, [550, 105])
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(550,105)) and (y in range(550,105)):
                    pygame.draw.rect(screen, (248,248,255), [550, 105, 120, 30])
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if next_button.collidepoint(x, y):
                    circle1_selected = False
                    circle2_selected = False
                    circle3_selected = False
                    player1 = not player1
                    player2 = not player2

        pygame.display.flip()
