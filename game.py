import enemy
import pygame
import ship
from bullet import Bullet
import effect
#create window
pygame.init()
pygame.mixer.init()
explosion_sound=pygame.mixer.Sound(r"C:\Users\Nathan Kimani\Desktop\game\Nathan-main\Nathan-main\explosion\explosion.wav")
shoot_sound=pygame.mixer.Sound(r"C:\Users\Nathan Kimani\Desktop\game\Nathan-main\Nathan-main\shoot\shoot.wav")
bg=pygame.image.load(r"C:\Users\Nathan Kimani\Desktop\game\Nathan-main\Nathan-main\Starry_night_Layer_8.png")
screan=pygame.display.set_mode((400,400))
mybullet=Bullet
allbullets = []
alleffects = []
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
                ship.myship.rectangle.centerx+=15
            if button.key == pygame.K_LEFT:
                ship.myship.rectangle.centerx-=15
            if button.key == pygame.K_UP:
                 ship.myship.rectangle.centery-=7
            if button.key == pygame.K_DOWN:
                ship.myship.rectangle.centery+=7
            # shoot
            if button.key == pygame.K_SPACE:
                shoot_sound.play()
                new_bullet=Bullet()
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
    screan.blit(bg, (0,-50))
    #drawing
    draw()
    screan.blit(newenemy.image, newenemy.rectangle)
    for enemy in allenemies:
        screan.blit(enemy.image,enemy.rectangle)
    enemynumber=0
    record_of_hit_enemy=[]
    for enemy in allenemies:
        for bullet in allbullets:
         if bullet.rectangle.centery<0:
            allbullets.remove(bullet)
            continue
         if  enemy.rectangle.colliderect(bullet.rectangle):
            print("ENEMY HIT!")
            allbullets.remove(bullet)
            neweffect=effect.Effect(enemy.rectangle.centerx,enemy.rectangle.centery-25)
            alleffects.append(neweffect)
            record_of_hit_enemy.append(enemy)
    for eff in alleffects:
        eff.show(screan)
    for myenemy in allenemies:
        if myenemy in record_of_hit_enemy:
            allenemies.remove(myenemy)
            explosion_sound.play()
    if len(allenemies)== 0:
        print("need enemies")
        import enemy
        for i in range (10):
            newenemy=enemy.Enemy()
            newenemy.rectangle.centerx=50+i*34
            newenemy.rectangle.centery=15
            allenemies.append(newenemy)
    pygame.display.flip()
                  















































