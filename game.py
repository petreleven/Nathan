import pygame
import ship
import bullet
#create window
pygame.init()
screan=pygame.display.set_mode((400,400))
mybullet=bullet.singlebullet
allbullet = []
def shoot():
    for botton in pygame.event.get():
        if botton.type == pygame.KEYDOWN:
            if botton.key == pygame.K_SPACE:
                print("shoot")
#move ship to center

ship.myship.rectangle.centerx=200
ship.myship.rectangle.centery=370
def draw():
    for b in allbullet:
        pygame.draw.rect(screan,color=b.color,rect=b.rectangle)
        b.rectangle.y+=0.4
        print(b.rectangle.y)
    pygame.draw.rect(screan,mybullet.color,mybullet.rectangle)
    screan.blit(ship.myship.image , ship.myship.rectangle)
    pygame.display.flip()
def moveship():
    for button in pygame.event.get():
        if button.type == pygame.KEYDOWN:
            if button.key == pygame.K_RIGHT:
                ship.myship.rectangle.centerx+=5
            if button.key == pygame.K_LEFT:
                ship.myship.rectangle.centerx-=5
           

            if button.key == pygame.K_UP:
                 ship.myship.rectangle.centery-=5
            if button.key == pygame.K_DOWN:
                ship.myship.rectangle.centery+=5
            if button.key == pygame.K_SPACE:
                new_bullet=bullet.bullet()
                new_bullet.rectangle.centerx=200
                new_bullet.rectangle.centery=200
                allbullet.append(new_bullet)
while True:
#detect keyboard clicks
    moveship()
    
    screan.fill((100,55,200))
    #drawing
    draw()
    shoot()





















































