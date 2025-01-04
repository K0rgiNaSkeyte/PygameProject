import pygame


def main():
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("The Elder Scrolls VI: In prison")
    screen.fill("black")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
