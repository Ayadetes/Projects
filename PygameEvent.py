import pygame
import random
pygame.init()

class sprite(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=position)

    def change_color(self):
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
colorchange_event = pygame.USEREVENT + 1

sprite_group = pygame.sprite.Group()

sprite1 = sprite((100, 100), (50, 50))
sprite2 = sprite((100, 100), (200, 50))

sprite_group.add(sprite1, sprite2)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == colorchange_event:
            for spr in sprite_group:
                spr.change_color()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        pygame.event.post(pygame.event.Event(colorchange_event))
        
    screen.fill((255, 255, 255))
    sprite_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)