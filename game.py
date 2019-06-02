import pygame
import os

def main():
    pygame.init()
    pygame.display.set_caption("Hello B)")
    screen = pygame.display.set_mode((800,600))

    menu_background = pygame.image.load(os.path.join("images", "background.png"))
    play_button = pygame.image.load(os.path.join("images", "basic_button.png")).convert()

    game_background = pygame.image.load(os.path.join("images", "game_background.png"))

    running = True
    MENU = True
    GAME = False

    while running:
        if MENU:
            screen.blit(menu_background, (5,5))
            screen.blit(play_button,(600, 40))
            pygame.display.flip()
        if GAME:
            screen.blit(game_background, (0,0))
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_button.get_rect().collidepoint(x, y):
                    print("IMAGE WAS CLICKED")
            if event.type == pygame.QUIT:
                running = False
if __name__ =="__main__":
    main()
