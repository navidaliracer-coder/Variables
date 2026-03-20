import math
import random
import pygame
import os

Screen_Width = 800
Screen_Height = 500
Player_Start_X = 370
Player_Start_Y = 380
Enemy_Start_Y_Min = 50
Enemy_Start_Y_Max = 150
Enemy_Speed_X = 4
Enemy_Speed_Y = 40
Bullet_Speed_Y = 10
Collision_Distant = 27

pygame.init()

screen = pygame.display.set_mode((Screen_Width, Screen_Height))

base_path = os.path.dirname(__file__)

background = pygame.image.load(os.path.join(base_path, 'Background.png'))
background = pygame.transform.scale(background, (Screen_Width, Screen_Height))

pygame.display.set_caption('SPACE INVADERS👾')
icon = pygame.image.load(os.path.join(base_path, 'ufo.png'))
pygame.display.set_icon(icon)

playerImg = pygame.image.load(os.path.join(base_path, 'player.png'))
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = Player_Start_X
playerY = Player_Start_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    img = pygame.image.load(os.path.join(base_path, 'enemy.png'))
    img = pygame.transform.scale(img, (64, 64))
    enemyImg.append(img)

    enemyX.append(random.randint(0, Screen_Width - 64))
    enemyY.append(random.randint(Enemy_Start_Y_Min, Enemy_Start_Y_Max))
    enemyX_change.append(Enemy_Speed_X)
    enemyY_change.append(Enemy_Speed_Y)

bulletImg = pygame.image.load(os.path.join(base_path, 'bullet.png'))
bulletImg = pygame.transform.scale(bulletImg, (32, 32))

bulletX = 0
bulletY = Player_Start_Y
bulletY_change = Bullet_Speed_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME 🛑 OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX ) ** 2 + (enemyY - bulletY) **2)
    return distance < Collision_Distant

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0

    playerX += playerX_change
    playerX = max(0, min(playerX, Screen_Width - 64))

    for i in range(num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= Screen_Width - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = Player_Start_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, Screen_Width - 64)
            enemyY[i] = random.randint(Enemy_Start_Y_Min, Enemy_Start_Y_Max)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = Player_Start_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()