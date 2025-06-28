import enemy
import pygame
import ship
import bullet
#create window
pygame.init()
screan=pygame.display.set_mode((400,400))
mybullet=bullet.singlebullet
allbullets = []
start_time=pygame.time.get_ticks()
allenemies = []
for i in range (10):
    newenemy=enemy.Enemy()
    newenemy.rectangle.centerx=50+i*34
    newenemy.rectangle.centery=15
    allenemies.append(newenemy)


#move ship to center

ship.myship.rectangle.centerx=200
ship.myship.rectangle.centery=370

def draw():
    for b in allbullets:
        pygame.draw.rect(screan,color=b.color,rect=b.rectangle)
        b.rectangle.y-=1

    screan.blit(ship.myship.image , ship.myship.rectangle)
    


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
                new_bullet=bullet.Bullet()
                new_bullet.rectangle.center = (ship.myship.rectangle.centerx, ship.myship.rectangle.centery)
                allbullets.append(new_bullet)

while True:
#detect keyboard clicks
    move_n_shoot()
    currenttime=pygame.time.get_ticks()
    if currenttime-start_time> 1000:
        #move enemies
        for enemy in allenemies:
            enemy.rectangle.centery+=10
        start_time=currenttime
    
    screan.fill((100,55,200))
    #drawing
    draw()
    screan.blit(newenemy.image, newenemy.rectangle)
    for enemy in allenemies:
        screan.blit(enemy.image,enemy.rectangle)

    for enemy in allenemies:
        for bullet in allbullets:
         if  enemy.rectangle.colliderect(bullet.rectangle):
            print("ENEMY HIT!")
    pygame.display.flip()
                  















































