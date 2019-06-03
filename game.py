import pygame
import os

def main():
    pygame.init()

    pygame.mixer.pre_init(44100,16,2,4096)
    pygame.display.set_caption("RED WEBBING")
    screen = pygame.display.set_mode((800,600))
    image = pygame.image.load(os.path.join("images", "background.png"))
    character_selection = pygame.image.load(os.path.join("images", "character_selection.png"))
    play_button_image = pygame.image.load(os.path.join("images", "basic_button.png")).convert()
    option_button_image = pygame.image.load(os.path.join("images", "option_button.png")).convert()
    pick_jose_image = pygame.image.load(os.path.join("images", "character_jose.png")).convert()
    pick_josette_image = pygame.image.load(os.path.join("images", "character_josette.png")).convert()
    menu_background = pygame.image.load(os.path.join("images", "background.png"))
    play_background = pygame.image.load(os.path.join("images", "playbackground.png"))
    option_background = pygame.image.load(os.path.join("images", "optionbackground.png"))
    screen.blit(image, (5,5))
    pygame.display.flip()

    pygame.mixer.music.load(os.path.join("src", "bgm.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    running = True
    MENU = True
    SELECTION = False
    GAME = False
    OPTION = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if MENU:
            screen.blit(menu_background, (5,5))
            play_button = pygame.draw.rect(screen, (190, 190, 255), [340, 430, 121, 61])
            screen.blit(play_button_image, [340, 430])

            option_button = pygame.draw.rect(screen, (190, 190, 255), [320, 500, 155, 61])
            screen.blit(option_button_image, [320, 500])

            pygame.display.flip()
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(340,460)) and (y in range(430,485)):
                    screen.blit(pick_jose_image, [121, 61])
                    print("Hovering over play button!")
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_button.collidepoint(x, y):
                    SELECTION = True
                    MENU = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if option_button.collidepoint(x, y):
                    OPTION = True
                    MENU = False
        if SELECTION:
            screen.blit(character_selection, (0,0))
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(200,400)) and (y in range(200,400)):
                    screen.blit(pick_jose_image, [130, 230])
                    print("Hovering over jose!")
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ( x in range(200,400)) and (y in range(200,400)):
                    print("Clicked on jose!")
                    SELECTION = False
                    GAME = True

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(500,700)) and (y in range(200,400)):
                    screen.blit(pick_josette_image, [480, 230])
                    print("Hovering over josette!")
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ( x in range(500,700)) and (y in range(200,400)):
                    print("Clicked on josette!")
                    SELECTION = False
                    GAME = True

            pygame.display.flip()

        if GAME:
            screen.blit(play_background, (5,5))
            import play
            pygame.display.flip()

        if OPTION:
            screen.blit(option_background, (5,5))
            pygame.display.flip()



if __name__ =="__main__":
    main()
