import pygame
import ship
import bullet
#create window
pygame.init()
screan=pygame.display.set_mode((400,400))
mybullet=bullet.singlebullet
allbullets = []




#move ship to center

ship.myship.rectangle.centerx=200
ship.myship.rectangle.centery=370

def draw():
    for b in allbullets:
        pygame.draw.rect(screan,color=b.color,rect=b.rectangle)
        b.rectangle.y-=1

    screan.blit(ship.myship.image , ship.myship.rectangle)
    pygame.display.flip()


def move_n_shoot():
    for button in pygame.event.get():
        if button.type == pygame.KEYDOWN:
            #moving the ship
            if button.key == pygame.K_RIGHT:
                ship.myship.rectangle.centerx+=7
            if button.key == pygame.K_LEFT:
                ship.myship.rectangle.centerx-=7
            if button.key == pygame.K_UP:
                 ship.myship.rectangle.centery-=7
            if button.key == pygame.K_DOWN:
                ship.myship.rectangle.centery+=7
            # shoot
            if button.key == pygame.K_SPACE:
                new_bullet=bullet.bullet()
                new_bullet.rectangle.center = (ship.myship.rectangle.centerx, ship.myship.rectangle.centery)
                print(new_bullet.rectangle.centerx)
                allbullets.append(new_bullet)

while True:
#detect keyboard clicks
    move_n_shoot()
    
    screan.fill((100,55,200))
    #drawing
    draw()






















































