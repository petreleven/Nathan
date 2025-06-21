import enemy
import pygame
import ship
import bullet


# create window
pygame.init()
screan = pygame.display.set_mode((400, 400))
mybullet = bullet.singlebullet
allbullets = []
# task create 10 enemies
allenemies = []
for i in range(10):
    # create and store the enemies
    newenemy = enemy.Enemy()
    newenemy.rectangle.centerx = 20 + i * 50
    newenemy.rectangle.centery = 10
    allenemies.append(newenemy)

# last_move_time = pygame.time.get_ticks()
# move ship to center

ship.myship.rectangle.centerx = 200
ship.myship.rectangle.centery = 370


def draw():
    for b in allbullets:
        pygame.draw.rect(screan, color=b.color, rect=b.rectangle)
        b.rectangle.y -= 1

    screan.blit(ship.myship.image, ship.myship.rectangle)


def move_n_shoot():
    for button in pygame.event.get():
        if button.type == pygame.KEYDOWN:
            if button.key == pygame.K_SPACE:
                new_bullet = bullet.bullet()
                new_bullet.rectangle.center = (
                    ship.myship.rectangle.centerx,
                    ship.myship.rectangle.centery,
                )
                print(new_bullet.rectangle.centerx)
                allbullets.append(new_bullet)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.myship.rectangle.centerx -= 1
    if keys[pygame.K_RIGHT]:
        ship.myship.rectangle.centerx += 1


while True:
    current_time = pygame.time.get_ticks()
    # detect keyboard clicks=
    move_n_shoot()
    screan.fill((100, 55, 200))
    # drawing
    draw()

    # lets draw all the 10 enemies
    for enemy in allenemies:
        screan.blit(enemy.image, enemy.rectangle)

    pygame.display.flip()
