import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My First Pygame Screen")
Background_Color = screen.fill((58,58,58))
running = True
Man = pygame.image.load("Man.png")
Resized = pygame.transform.scale(Man, (300,300))
screen.blit(Resized, (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()