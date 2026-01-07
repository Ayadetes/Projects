import math
import pygame
import time

PlayerData = {"ProfilePic": pygame.image.load("Spaceship.png"), "PosX": 370, "PosXChange": 0, "PosY": 380, "Speed": 5}
EnemyData = [[],[],[],[],[],[],[],[]]
for i in range(7):
    EnemyData[i].append(pygame.image.load("Enemy.png"))
    EnemyData[i].append(0 + i * (736 / 7))
    EnemyData[i].append(150 - i * 20)
    EnemyData[i].append(5)
    EnemyData[i].append(30)
    EnemyData[i].append(True)  # Alive status
screen_width = 800
screen_height = 500
Bullet_speed_y = 10
collision_distance = 27
PlayerSpeed = PlayerData["Speed"]
playerX = PlayerData["PosX"]
playerY = PlayerData["PosY"]
playerImg = PlayerData["ProfilePic"]
playerX_change = 0

pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders: A Teacher's Copy")
background = pygame.image.load("MarioBG.png")
pygame.display.set_icon(playerImg)

bulletImg = pygame.image.load("Bullet.png")
bulletx = 0
bullety = playerY
bulletx_change = 0
bullety_change = Bullet_speed_y
bulletfire = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def win_text():
    win_text = over_font.render("YOU WIN", True, (255, 255, 255))
    screen.blit(win_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    if EnemyData[i][5]:  # Check if enemy is alive
        screen.blit(EnemyData[i][0], (x, y))
    else:
        pass  # Enemy is dead; do not draw

def fire_bullet(x, y):
    global bulletfire
    bulletfire = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletx, bullety):
    distance = math.sqrt((enemyX - bulletx) ** 2 + (enemyY - bullety) ** 2)
    return distance < collision_distance

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -PlayerSpeed
            if event.key == pygame.K_RIGHT:
                playerX_change = PlayerSpeed
            if event.key == pygame.K_SPACE:
                if bulletfire == "ready":
                    bulletx = playerX
                    fire_bullet(bulletx, bullety)
                    Bullet_State = "debounce"
                    time.sleep(0.2)
                    Bullet_state = "ready"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    playerX = max(0, min(playerX, 736))

    for i in range(7):
        if EnemyData[i][2] > 340 and EnemyData[i][5]:
            for j in range(7):
                EnemyData[j][2] = 2000
            game_over_text()
        elif all(not EnemyData[k][5] for k in range(7)):
            win_text()
            break

        EnemyData[i][1] += EnemyData[i][3]
        if EnemyData[i][1] <= 0:
            EnemyData[i][3] = 4
            EnemyData[i][2] += 20
        elif EnemyData[i][1] >= 736:
            EnemyData[i][3] = -4
            EnemyData[i][2] += 20
        collision = isCollision(EnemyData[i][1], EnemyData[i][2], bulletx, bullety)
        if collision and EnemyData[i][5]:
            bullety = playerY
            bulletfire = "ready"
            score_value += 1
            EnemyData[i][5] = False  # Mark enemy as dead

        enemy(EnemyData[i][1], EnemyData[i][2], i)

    if bullety <= 0:
        bullety = playerY
        bulletfire = "ready"
    elif bulletfire == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
        