import pygame
class ship:
    def __init__(self):
        self.health =100
        self.image=pygame.image.load(r"C:\Users\Nathan Kimani\Desktop\game\Nathan-main\Nathan-main\OIP-removebg-preview (2).png")
        self.image =pygame.transform.scale(self.image,(100,100))
        self.rectangle=self.image.get_rect()

myship= ship()
print(myship.health)


















