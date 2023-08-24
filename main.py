import pygame
import random


#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('./Assets/Space.png')
background_image = pygame.transform.scale(background, (840, 600))


#Title and Icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('./Assets/nave-espacial.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('./Assets/spaceship.png')
playerX = 357.5
playerY = 480
playerX_change = 0
nova_imagem = pygame.transform.scale(playerImg, (75, 75))

#Enemy
enemyImg = pygame.image.load('./Assets/alien.png')
enemyX = random.randint(0, 777)
enemyY = random.randint(50, 150)
enemyX_change = 3.5
enemyY_change = 40

enemy_imagem = pygame.transform.scale(enemyImg, (45, 45))

def player(x,y):
    #blit basically means draw
    screen.blit(nova_imagem, (x, y))

def enemy(x,y):
    #blit basically means draw
    screen.blit(enemy_imagem, (x, y))


#Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0,0,0))
    #Background Image
    screen.blit(background_image, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_d:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                print("Keystroke has been released")
                playerX_change = 0
    #Player movement
    playerX += playerX_change

    if playerX <= -75.0001:
        playerX = 800
    elif playerX >= 800:
        playerX = -75


    #enemy movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 3.5
        enemyY += enemyY_change
    elif enemyX >= 755:
        enemyX_change = -3.5
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
