import pygame
import os

def main():
    pygame.init()
    pygame.display.set_caption("Hello B)")
    screen = pygame.display.set_mode((800,600))

    menu_background = pygame.image.load(os.path.join("images", "background.png"))
    play_button_image = pygame.image.load(os.path.join("images", "basic_button.png")).convert()
    play_button = pygame.draw.rect(screen, (190, 190, 255), [500, 200, 121, 61])
    character_selection = pygame.image.load(os.path.join("images", "character_selection.png"))

    running = True
    MENU = True
    SELECTION = False
    GAME = False

    while running:
        if MENU:
            screen.blit(menu_background, (5,5))
            play_button = pygame.draw.rect(screen, (190, 190, 255), [600, 40, 121, 61])
            screen.blit(play_button_image, [600, 40])
            pygame.display.flip()
        if SELECTION:
            screen.blit(character_selection, (0,0))
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_button.collidepoint(x, y):
                    SELECTION = True
                    MENU = False
            if event.type == pygame.QUIT:
                running = False

if __name__ =="__main__":
    main()
