import pygame
import os

def main():
    pygame.init()

    pygame.mixer.pre_init(44100,16,2,4096)
    pygame.display.set_caption("RED WEBBING")
    screen = pygame.display.set_mode((800,600))

    image = pygame.image.load(os.path.join("images", "menu_background.png"))
    character_selection = pygame.image.load(os.path.join("images", "character_selection.png"))
    blank_background = pygame.image.load(os.path.join("images", "blank_background.png"))
    menu_background = pygame.image.load(os.path.join("images", "menu_background.png"))
    play_background = pygame.image.load(os.path.join("images", "playbackground.png"))
    option_background = pygame.image.load(os.path.join("images", "optionbackground.png"))

    spider_pop_up = pygame.image.load(os.path.join("images", "spider-pop.png"))
    dropdown_spider = pygame.image.load(os.path.join("images", "dropdown_spider.png"))

    play_button_image = pygame.image.load(os.path.join("images", "basic_button.png")).convert()
    option_button_image = pygame.image.load(os.path.join("images", "option_button.png")).convert()
    back_button_image = pygame.image.load(os.path.join("images", "back_button.png")).convert()

    pick_jose_image = pygame.image.load(os.path.join("images", "character_jose.png")).convert()
    pick_josette_image = pygame.image.load(os.path.join("images", "character_josette.png")).convert()


    screen.blit(blank_background, (0,0))
    pygame.display.flip()

    pygame.mixer.music.load(os.path.join("src", "bgm.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    fpsClock = pygame.time.Clock()
    running = True
    MENU = True
    SELECTION = False
    GAME = False
    OPTION = False

    spiderX= 800;
    optionX= -195;
    dropdown1Y = -100;
    dropdown2Y = -100;
    dropdown3Y = -100;

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if MENU:
            if spiderX > -10:
                spiderX -= 10 ;
                screen.blit(spider_pop_up , (spiderX, -100) )
                pygame.display.update()
                fpsClock.tick(100)
                if spiderX < 200:
                    dropdown1Y += 10 ;
                    screen.blit(dropdown_spider , (620, dropdown1Y) )
                    pygame.display.update()
                    fpsClock.tick(100)
                if spiderX < 320:
                    dropdown2Y += 10 ;
                    screen.blit(dropdown_spider , (680, dropdown2Y) )
                    pygame.display.update()
                    fpsClock.tick(100)
                if spiderX > 100:
                    dropdown3Y += 20 ;
                    screen.blit(dropdown_spider , (130, dropdown3Y) )
                    pygame.display.update()
                    fpsClock.tick(100)
                if spiderX > 600:
                    optionX += 10 ;
                    screen.blit(option_button_image, [optionX, 20])
                    pygame.display.update()
                    fpsClock.tick(100)
            else:
                screen.blit(menu_background, (0,0))
                play_button = pygame.draw.rect(screen, (190, 190, 255), [330, 460, 121, 61])
                screen.blit(play_button_image, [330, 460])

                option_button = pygame.draw.rect(screen, (190, 190, 255), [-5, 20, 155, 61])
                screen.blit(option_button_image, [-5, 20])
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if ( x in range(330,470)) and (y in range(460,520)):
                    screen.blit(spider_pop_up, [340, 424])
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
            pygame.display.flip()

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
                    JOSE = True
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
                    JOSETTE = True
                    GAME = True

            pygame.display.flip()

        if GAME:
            screen.blit(play_background, (5,5))
            import play
            pygame.display.flip()

        if OPTION:
            screen.blit(option_background, (5,5))
            back_button = pygame.draw.rect(screen, (190, 190, 255), [580, 500, 121, 61])
            screen.blit(back_button_image, [580, 500])
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if back_button.collidepoint(x, y):
                    OPTION = False
                    SELECTION = False
                    MENU = True
            pygame.display.flip()



if __name__ =="__main__":
    main()
