import pygame
pygame.init()
#Tweaks
DefaultSpeed = 5


class Player1(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()  

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= DefaultSpeed
        if keys[pygame.K_RIGHT]:
            self.rect.x += DefaultSpeed
        if keys[pygame.K_UP]:
            self.rect.y -= DefaultSpeed
        if keys[pygame.K_DOWN]:
            self.rect.y += DefaultSpeed

class Player2(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()  

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= DefaultSpeed
        if keys[pygame.K_d]:
            self.rect.x += DefaultSpeed
        if keys[pygame.K_w]:
            self.rect.y -= DefaultSpeed
        if keys[pygame.K_s]:
            self.rect.y += DefaultSpeed
    
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Sprites")

player1 = Player1((255, 215, 0), 50, 50)
player2 = Player2((0, 215, 255), 50, 50)
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)