import pygame
import os

player1 = True
player2 = False

bcircle1_selected = False
bcircle2_selected = False
bcircle3_selected = False

rcircle1_selected = False
rcircle2_selected = False

show_next_button = False

coords1 = False
coords2 = False

blue_lines1 = []
blue_lines2 = []
red_lines1 = []
red_lines2 = []

pygame.init()
screen = screen = pygame.display.set_mode((800,600))
play_background = pygame.image.load(os.path.join("images", "playbackground.png"))
next_button_image = pygame.image.load(os.path.join("images", "next_button.png"))
two_circles_notice = pygame.image.load(os.path.join("images", "two_circles_notice.png"))
player_1_turn = pygame.image.load(os.path.join("images", "player_1_turn.png"))
player_2_turn = pygame.image.load(os.path.join("images", "player_2_turn.png"))

running = True

while running:
    screen.blit(play_background, (0,0))

    bcircle1 = pygame.draw.circle(screen, (0,127,255), (200, 200), 6, 0)
    bcircle2 = pygame.draw.circle(screen, (0,127,255), (300, 300), 6, 0)
    bcircle3 = pygame.draw.circle(screen, (0,127,255), (550, 450), 6, 0)

    rcircle1 = pygame.draw.circle(screen, (255,69,0), (450, 250), 6, 0)
    rcircle2 = pygame.draw.circle(screen, (255,69,0), (150, 300), 6, 0)

    for x in blue_lines1:
        for y in blue_lines2:
            pygame.draw.line(screen, (0,127,255), (x), (y), 4)

    for x in red_lines1:
        for y in red_lines2:
            pygame.draw.line(screen, (255,69,0), (x), (y), 4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if player1:
            screen.blit(player_1_turn, [20, 20])
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(195,211)) and (y in range(195,211)):
                    pygame.draw.circle(screen, (248,248,255), (200, 200), 7, 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if bcircle1.collidepoint(x, y):
                    bcircle1_selected = not bcircle1_selected
                    if coords1 == False:
                        coords1 = (200, 200)
                    else:
                        if coords2 == False:
                            coords2 = (200, 200)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(295,311)) and (y in range(295,311)):
                    pygame.draw.circle(screen, (248,248,255), (300, 300), 7, 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if bcircle2.collidepoint(x, y):
                    bcircle2_selected = not bcircle2_selected
                    if coords1 == False:
                        coords1 = (300, 300)
                    else:
                        if coords2 == False:
                            coords2 = (300, 300)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(545,511)) and (y in range(445,461)):
                    pygame.draw.circle(screen, (248,248,255), (550, 450), 7, 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if bcircle3.collidepoint(x, y):
                    bcircle3_selected = not bcircle3_selected
                    if coords1 == False:
                        coords1 = (550, 450)
                    else:
                        if coords2 == False:
                            coords2 = (550, 450)
            if bcircle1_selected:
                pygame.draw.circle(screen, (248,248,255), (200, 200), 8, 3)
                selected = 0
                circles = [bcircle1_selected, bcircle2_selected, bcircle3_selected]
                for x in circles:
                    if x == True:
                        selected += 1
                if selected > 2:
                    screen.blit(two_circles_notice, [500, 100])
                if selected == 2:
                    show_next_button = True
                else:
                    show_next_button = False
            if bcircle2_selected:
                pygame.draw.circle(screen, (248,248,255), (300, 300), 8, 3)
                selected = 0
                circles = [bcircle1_selected, bcircle2_selected, bcircle3_selected]
                for x in circles:
                    if x == True:
                        selected += 1
                if selected > 2:
                    screen.blit(two_circles_notice, [500, 100])
                if selected == 2:
                    show_next_button = True
                else:
                    show_next_button = False
            if bcircle3_selected:
                pygame.draw.circle(screen, (248,248,255), (550, 450), 8, 3)
                selected = 0
                circles = [bcircle1_selected, bcircle2_selected, bcircle3_selected]
                for x in circles:
                    if x == True:
                        selected += 1
                if selected > 2:
                    screen.blit(two_circles_notice, [500, 100])
                if selected == 2:
                    show_next_button = True
                else:
                    show_next_button = False

        if player2:
            screen.blit(player_2_turn, [20, 20])
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(450,250)) and (y in range(450,250)):
                    pygame.draw.circle(screen, (248,248,255), (450, 250), 7, 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if rcircle1.collidepoint(x, y):
                    rcircle1_selected = not rcircle1_selected
                    if coords1 == False:
                        coords1 = (450, 250)
                    else:
                        if coords2 == False:
                            coords2 = (450, 250)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(150,300)) and (y in range(150,300)):
                    pygame.draw.circle(screen, (248,248,255), (150, 300), 7, 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if rcircle2.collidepoint(x, y):
                    rcircle2_selected = not rcircle2_selected
                    if coords1 == False:
                        coords1 = (150, 300)
                    else:
                        if coords2 == False:
                            coords2 = (150, 300)
            if rcircle1_selected:
                pygame.draw.circle(screen, (248,248,255), (450, 250), 8, 3)
                selected = 0
                circles = [rcircle1_selected, rcircle2_selected]
                for x in circles:
                    if x == True:
                        selected += 1
                if selected > 2:
                    screen.blit(two_circles_notice, [500, 100])
                if selected == 2:
                    show_next_button = True
                else:
                    show_next_button = False
            if rcircle2_selected:
                pygame.draw.circle(screen, (248,248,255), (150, 300), 8, 3)
                selected = 0
                circles = [rcircle1_selected, rcircle2_selected]
                for x in circles:
                    if x == True:
                        selected += 1
                if selected > 2:
                    screen.blit(two_circles_notice, [500, 100])
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
                    if coords1 != False and coords2 != False:
                        if player1:
                            # blue_lines.append(pygame.draw.line(screen, (0,127,255), (coords1), (coords2), 4))
                            blue_lines1.append(coords1)
                            blue_lines2.append(coords2)
                        if player2:
                            # red_lines.append(pygame.draw.line(screen, (255,69,0), (coords1), (coords2), 4))
                            red_lines1.append(coords1)
                            red_lines2.append(coords2)
                    bcircle1_selected = False
                    bcircle2_selected = False
                    bbcircle3_selected = False

                    rcircle1_selected = False
                    rcircle2_selected = False

                    player1 = not player1
                    player2 = not player2

                    coords1 = False
                    coords2 = False


        pygame.display.flip()
