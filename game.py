import pygame
import os

def main():
    pygame.init()
    pygame.mixer.pre_init(44100,16,2,4096)
    pygame.display.set_caption("Connect!)")

    screen = pygame.display.set_mode((800,600))
    image = pygame.image.load(os.path.join("images", "background.png"))
    screen.blit(image, (5,5))
    pygame.display.flip()

    pygame.mixer.music.load(os.path.join("src", "bgm.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
if __name__ =="__main__":
    main()