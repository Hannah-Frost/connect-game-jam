import pygame
import os

def main():
    pygame.init()
    pygame.display.set_caption("Hello B)")

    screen = pygame.display.set_mode((640,480))
    image = pygame.image.load(os.path.join("images", "background.png"))
    screen.blit(image, (5,5))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
if __name__ =="__main__":
    main()
