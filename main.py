import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

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
enemyX = 357.5
enemyY = 480
enemyX_change = 0
enemy_imagem = pygame.transform.scale(enemyImg, (75, 75))

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -0.3
            if event.key == pygame.K_d:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                print("Keystroke has been released")
                playerX_change = 0
    playerX += playerX_change

    if playerX <= -75.0001:
        playerX = 800
    elif playerX >= 800:
        playerX = -75

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
